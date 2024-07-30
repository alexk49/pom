#!/usr/bin/env python3
import argparse
from tkinter import Tk

from timers import Timer, TimerGUI


def set_arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--time",
        type=str,
        help="Pass time as string to set timer",
    )
    parser.add_argument(
        "-s",
        "--sound",
        action="store_true",
        help="Switch for playing sound at end of timer",
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
        timer = Timer(time_string=args.time, sound_on_finish=args.sound)

        timer.start_countdown()


if __name__ == "__main__":
    main()
