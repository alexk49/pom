import time
from typing import Tuple
from functools import partial

from tkinter import Tk, Entry
from tkinter import ttk


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


def start_countdown(timer_textbox: Entry, t: str):
    """Starts countdown of timer
    arg is always given as string from command line
    and from gui but is converted to int"""
    print(t)

    t = convert_input_time(t)

    while t >= 0:
        mins, secs = convert_time(t)
        time_string = print_time(mins, secs)
        
        # update timer_textbox display
        timer_textbox.delete(0, "end")
        timer_textbox.insert(0, time_string)
        timer_textbox.update()

        t = update_time(t)


def pause_countdown(t):
    pass


def update_timer_display(timer_textbox: Entry, t: str):
    """takes time as string variable: 00:00
    and sets timer textbox to given value"""
    pass


def set_timer(timer_textbox: Entry):
    """gets time variable and passes it to start_countdown

    This is in separate function as you can't call a function
    in the tkinter command"""
    t = timer_textbox.get()
    start_countdown(timer_textbox, t)


def set_pause(timer_textbox: Entry):
    """gets time variable and passes it to pause_countdown
    
    This is in separate function as you can't call a function
    in the tkinter command"""
    t = timer_textbox.get()
    pause_countdown(t)


def main():
    root = Tk()

    frame = ttk.Frame(root, padding=40)
    frame.grid()

    timer_textbox = Entry(frame, width=10, borderwidth=5)
    timer_textbox.grid(row=0, column=0, padx=10, pady=10)
    timer_textbox.insert(0, "00:00")

    ttk.Button(frame, text="Start", command=partial(set_timer, timer_textbox)).grid(column=0, row=1, padx=10)

    ttk.Button(frame, text="Pause", command=partial(set_pause, timer_textbox)).grid(column=1, row=1, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()
