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


def start_countdown(t):
    while t != 0:
        mins, secs = convert_time(t)
        print_time(mins, secs)
        t = update_time(t)
    print("finished!")


def main():
    t = int(input("enter time in seconds: "))
    run_countdown(t)


if __name__ == "__main__":
    main()
