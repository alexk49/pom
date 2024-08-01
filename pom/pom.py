#!/usr/bin/env python3
import argparse
import threading
from tkinter import Tk

from timers import TimerGUI, TimerCLI


def set_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--time",
        type=str,
        help="Pass time in format: mm:ss to set timer. If the time is passed as just a number, it will read as seconds.",
    )
    parser.add_argument(
        "-s",
        "--sound",
        action="store_true",
        help="Switch for playing sound at end of timer, this is set to off by default.",
    )
    return parser


def run_gui():
    root = Tk()
    display = TimerGUI(root)
    if display.pause:
        display.frame.focus()
    else:
        display.timer_textbox.focus()

    root.mainloop()


def main():
    parser = set_arg_parser()
    args = parser.parse_args()

    if args.time is None:
        run_gui()
    else:
        timer = TimerCLI(time_string=args.time, sound_on_finish=args.sound)

        threading.Thread(target=timer.key_listener).start()

        threading.Thread(target=timer.start_countdown).start()


if __name__ == "__main__":
    main()
