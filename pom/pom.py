#!/usr/bin/env python3
import os
import time
import platform
from typing import Tuple
from functools import partial
from threading import Event
from shutil import which
from subprocess import Popen

from tkinter import Tk, Entry, BooleanVar
from tkinter import ttk

# global event handler
# set when countdown is started
# and cleared when countdown is paused
PAUSE = Event()

windows_sound_file_path = os.path.join("sounds", "bell.wav")
linux_sound_file_path = os.path.join("sounds", "bell.mp3")

LAST_INDEX = -1


def update_time(t: int) -> int:
    """deincrement time by 1 second
    >>> update_time(30)
    29
    """
    time.sleep(1)
    t -= 1
    return t


def convert_time(t: int) -> Tuple[int, int]:
    """Time passed as seconds string converted to mins, secs
    >>> convert_time(70)
    (1, 10)
    """
    mins, secs = divmod(t, 60)
    return mins, secs


def print_time(mins: int, secs: int) -> str:
    """Print time to screen in format 00:00
    and also, returns string as variable
    >>> print_time(25, 00)
    25:00
    '25:00'
    """
    timer = "{:02d}:{:02d}".format(mins, secs)
    print(timer)
    return timer


def convert_input_time(string_time: str) -> int:
    """time passed as string like:
    02:05
    converted to seconds.
    If time passed without colon from command line
    will just return int value
    >>> convert_input_time("02:00")
    120
    >>> convert_input_time("20")
    20
    """
    if ":" not in string_time:
        return int(string_time)
    mins, secs = string_time.split(":")
    t = (int(mins) * 60) + int(secs)
    return t


def start_countdown(timer_textbox: Entry, time_string: str, sound_on_finish: BooleanVar):
    """Starts countdown of timer and clears global Event handler.
    arg can be given as string from command line
    and from gui in form 00:00 but both are converted to int
    """
    PAUSE.clear()

    t: int = convert_input_time(time_string)

    while not PAUSE.is_set() and t >= 0:
        mins, secs = convert_time(t)
        time_string = print_time(mins, secs)

        update_timer_display(timer_textbox, time_string)

        t = update_time(t)

    # timer counts down to 0
    # meaning it increments down to -1
    if t == -1 and sound_on_finish.get():
        playsound()


def pause_countdown(timer_textbox: Entry, time_string: str, sound_on_finish):
    """Takes time as string in form: 00:00,
    and pauses timer on given value

    Updates global Event handler PAUSE which stops countdown

    If PAUSE is already sets then works as toggle and restarts countdown
    """
    if PAUSE.is_set():
        start_countdown(timer_textbox, time_string, sound_on_finish)
    else:
        PAUSE.set()
        update_timer_display(timer_textbox, time_string)


def update_timer_display(timer_textbox: Entry, time_string: str):
    """takes time as string variable: 00:00
    and sets timer textbox to given value"""
    timer_textbox.delete(0, "end")
    timer_textbox.insert(0, time_string)
    timer_textbox.update()


def set_timer(timer_textbox: Entry, sound_on_finish: BooleanVar):
    """gets time variable and passes it to start_countdown

    This is in separate function as you can't execute a function in the tkinter command.
    And Entry.get() is required to get time value
    """
    t = timer_textbox.get()
    start_countdown(timer_textbox, t, sound_on_finish)


def set_pause(timer_textbox: Entry, sound_on_finish):
    """gets time variable and passes it to pause_countdown

    This is in separate function as you can't execute a function in the tkinter command.
    And Entry.get() is required to get time value.
    """
    t = timer_textbox.get()
    pause_countdown(timer_textbox, t, sound_on_finish)


def keyboard_shortcuts(event, timer_textbox: Entry, sound_on_finish: BooleanVar):
    """Handles all keyboard shortcuts"""
    key = event.keysym
    time_string = timer_textbox.get()
    if PAUSE.is_set() and (key == "Return" or key == "space"):
        start_countdown(timer_textbox, time_string, sound_on_finish)
    elif not PAUSE.is_set() and (key == "Return" or key == "space"):
        PAUSE.set()
        update_timer_display(timer_textbox, time_string)
    elif key.isdigit():
        time_string = increment_display_value(key, time_string)
        update_timer_display(timer_textbox, time_string)


def tool_exists(name: str) -> bool:
    """Check whether given `name` is on PATH and marked as executable."""
    return which(name) is not None


def playsound():
    """Detects operating system and then plays sound file

    If on a non windows system then mpg123 is required"""
    if platform.platform() != "Windows" and tool_exists("mpg123"):
        Popen(["mpg123", linux_sound_file_path])
    else:
        import winsound

        winsound.PlaySound(windows_sound_file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)


def validate_timer_input(input_char: str, type_of_action: str, potential_display: str):
    """basic validation of timer input based on:

    https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter#4140988

    Tkinter passes in special values to function:
    # %S = the text string being inserted or deleted, if any
    # %d = Type of action (1=insert, 0=delete, -1 for others)
    # %P = value of the entry if the edit is allowed
    """
    if type_of_action == "1":  # input
        # input value should always match format 00:00
        values = potential_display.split(":")
        if len(values) > 2:
            return False
        mins, secs = values

        if not mins.isdigit() or not secs.isdigit() or len(mins) != 2 or len(secs) != 2:
            return False

    # stop deletion of : char
    if type_of_action == "0" and input_char == ":":
        return False
    return True


def increment_display_value(new_digit: str, display: str) -> str:
    """Increments display when a digit is pressed.
    >>> increment_display_value("5", "00:00")
    '00:05'
    >>> increment_display_value("4", "00:05")
    '00:54'
    >>> increment_display_value("3", "00:54")
    '05:43'
    >>> increment_display_value("2", "05:43")
    '54:32'
    """
    global LAST_INDEX
    # stop reassignment of :
    if LAST_INDEX == -3:
        LAST_INDEX -= 1
    # reassign to start if get to end of string
    if LAST_INDEX == -6:
        LAST_INDEX = -1

    dis = list(display)

    # just update last char
    if LAST_INDEX == -1:
        dis[LAST_INDEX] = new_digit
    else:
        dis.pop(0)
        dis.append(new_digit)
        # reassign : to be central value
        dis[1] = dis[2]
        dis[2] = ":"
    dis = "".join(dis)
    LAST_INDEX -= 1
    return dis


def main():
    root = Tk()

    sound_on_finish = BooleanVar()

    frame = ttk.Frame(root, padding=40)
    frame.grid()

    timer_textbox = Entry(frame, width=10, borderwidth=5, validate="key")
    timer_textbox["validatecommand"] = (timer_textbox.register(validate_timer_input), "%S", "%d", "%P")
    timer_textbox.grid(row=0, column=0, padx=10, pady=10)
    timer_textbox.insert(0, "00:00")

    ttk.Button(frame, text="Start", command=partial(set_timer, timer_textbox, sound_on_finish)).grid(
        column=0, row=1, padx=10
    )

    ttk.Button(frame, text="Pause", command=partial(set_pause, timer_textbox, sound_on_finish)).grid(
        column=1, row=1, padx=10
    )

    ttk.Checkbutton(frame, text="Play sound", variable=sound_on_finish).grid(column=1, row=2, padx=20, pady=20)

    root.bind_all(
        "<KeyPress>",
        lambda event: keyboard_shortcuts(event, timer_textbox=timer_textbox, sound_on_finish=sound_on_finish),
    )

    if PAUSE.set():
        frame.focus()
    else:
        timer_textbox.focus()

    root.mainloop()


if __name__ == "__main__":
    main()
