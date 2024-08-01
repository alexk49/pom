import os
import platform
import time
from shutil import which
from subprocess import Popen
from typing import Tuple

from tkinter import Entry, BooleanVar
from tkinter import ttk


class Timer:
    """Timer class used in CLI, and base class for GUI"""

    def __init__(self, time_string="00:00", sound_on_finish=False, *args, **kwargs):
        self.pause: bool = False
        self.sound_on_finish: bool = sound_on_finish

        self.windows_sound_file_path: str = os.path.join("sounds", "bell.wav")
        self.linux_sound_file_path: str = os.path.join("sounds", "bell.mp3")

        self.time_string: str = time_string
        self.time: int = Timer.convert_input_time(self.time_string)

    @staticmethod
    def convert_input_time(string_time) -> int:
        """converts time passed as string like 02:05
        to time in seconds.

        If time passed without colon from command line
        will just return int value.

        >>> Timer.convert_input_time("02:03")
        123
        >>> Timer.convert_input_time("2")
        2
        """
        if ":" not in string_time:
            return int(string_time)
        mins, secs = string_time.split(":")
        t = (int(mins) * 60) + int(secs)
        return t

    def start_countdown(self):
        """Starts countdown of timer and clears global Event handler.
        arg can be given as string from command line
        and from gui in form 00:00 but both are converted to int
        """
        self.pause = False

        while not self.pause and self.time >= 0:
            mins, secs = self.convert_time()
            self.update_time_string(mins, secs)

            print(self.time_string)
            self.update_time()

        self.check_for_sound()

    def check_for_sound(self):
        # timer counts down to 0
        # meaning it increments down to -1
        if self.time == -1 and self.sound_on_finish:
            self.playsound()

    def convert_time(self) -> Tuple[int, int]:
        """Time passed as seconds string converted to mins, secs
        >>> t = Timer()
        >>> t.time = 40
        >>> t.convert_time()
        (0, 40)
        """
        mins, secs = divmod(self.time, 60)
        return mins, secs

    def update_time_string(self, mins: int, secs: int):
        """
        Updates passed ints to time string in format mm:ss
        >>> t = Timer()
        >>> t.update_time_string(2, 35)
        >>> t.time_string
        '02:35'
        """
        self.time_string = "{:02d}:{:02d}".format(mins, secs)

    def update_time(self):
        """deincrement time by 1 second
        >>> t = Timer()
        >>> t.time = 3
        >>> t.update_time()
        >>> t.time
        2
        """
        time.sleep(1)
        self.time -= 1

    def playsound(self):
        """Detects operating system and then plays sound file

        If on a non windows system then mpg123 is required"""
        if platform.platform() != "Windows" and which("mpg123") is not None:
            Popen(["mpg123", self.linux_sound_file_path])
        else:
            import winsound

            winsound.PlaySound(self.windows_sound_file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def pause_countdown(self):
        if self.pause is True:
            self.pause = False
            self.start_countdown()
        else:
            self.pause = True


class TimerCLI(Timer):
    """Additional Class to provide keyboard listener
    so Timer can be paused when run as CLI only."""
    def __init__(self, time_string="00:00", sound_on_finish=False, *args, **kwargs):
        super().__init__(time_string, sound_on_finish, *args, **kwargs)
        
        # works as mainloop
        self.running = True

    def key_listener(self):
        """listens for Enter key"""
        while self.running:
            input()
            self.pause_countdown()

class TimerGUI(Timer):
    """Inherits from Timer and adds GUI"""

    def __init__(self, root):
        super().__init__()
        self.root = root

        self.frame = ttk.Frame(root, padding=40)
        self.frame.grid()

        self.timer_textbox = Entry(self.frame, width=10, borderwidth=5, validate="key")
        self.timer_textbox["validatecommand"] = (
            self.timer_textbox.register(self.validate_timer_input),
            "%S",
            "%d",
            "%P",
            "%i",
        )

        self.timer_textbox.grid(row=0, column=0, padx=10, pady=10)
        self.timer_textbox.insert(0, "00:00")

        self.start_button = ttk.Button(self.frame, text="Start", command=self.start_countdown).grid(
            column=0, row=1, padx=10
        )

        self.pause_button = ttk.Button(self.frame, text="Pause", command=self.pause_countdown).grid(
            column=1, row=1, padx=10
        )

        self.sound_on_finish = BooleanVar()
        self.sound_button = ttk.Checkbutton(self.frame, text="Play sound", variable=self.sound_on_finish).grid(
            column=1, row=2, padx=20, pady=20
        )

        # keyboard shortcuts
        # pause_countdown will also start countdown when pause is false
        self.root.bind("<Return>", lambda event: self.pause_countdown())
        self.root.bind("<space>", lambda event: self.pause_countdown())
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def validate_timer_input(self, input_char: str, type_of_action: str, potential_display: str, index_of_char: str):
        """basic validation of timer input based on:

        https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter#4140988

        Tkinter passes in special values to function:
        # %S = the text string being inserted or deleted, if any
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %P = value of the entry if the edit is allowed
        # %i = index of char string to be inserted/deleted, or -1
        """
        if type_of_action == "1":  # input
            # input value should always match format 00:00
            values = potential_display.split(":")
            if len(values) > 2:
                return False
            mins, secs = values

            if not mins.isdigit() or not secs.isdigit() or len(mins) > 2 or len(secs) > 2:
                return False

        # stop deletion of : char
        if type_of_action == "0" and input_char == ":":
            return False
        return True

    def start_countdown(self):
        """
        GUI App needs self.time value from timer_textbox display
        Whereas for CLI the self.time value is given as an arg
        """
        self.time = self.convert_input_time(self.timer_textbox.get())
        super().start_countdown()

    def check_for_sound(self):
        """
        sound_on_finish when gui running
        uses BooleanVar from tkinter
        meaning actual value needs .get()
        command line app just uses bool value
        """
        if self.time == -1 and self.sound_on_finish.get():
            self.playsound()

    def update_time_string(self, mins, secs):
        """Calls Timer.update_time_string
        And then updates GUI display"""
        super().update_time_string(mins, secs)
        self.update_timer_display()

    def update_timer_display(self):
        """takes time as string variable: 00:00
        and sets timer textbox to given value"""
        self.timer_textbox.delete(0, "end")
        self.timer_textbox.insert(0, self.time_string)
        self.timer_textbox.update()

