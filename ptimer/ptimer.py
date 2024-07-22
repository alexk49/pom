import time
from typing import Tuple

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


def start_countdown(t: str):
    """Starts countdown of timer
    arg is always given as string from command line
    and from gui but is converted to int"""
    print(t)

    t = convert_input_time(t)

    while t != 0:
        mins, secs = convert_time(t)
        print_time(mins, secs)
        t = update_time(t)
    print("finished!")


def main():
    t = convert_input_time(input("enter time in seconds: "))
    start_countdown(t)


if __name__ == "__main__":
    main()
