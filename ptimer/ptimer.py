import time
from typing import Tuple


def updateTime(t: int) -> int:
    """deincrement time by 1 second
    >>> updateTime(30)
    29
    """
    time.sleep(1)
    t -= 1
    return t


def convertTime(t: int) -> Tuple[int, int]:
    """Time passed as seconds string converted to mins, secs
    >>> convertTime(70)
    (1, 10)
    """
    mins, secs = divmod(t, 60)
    return mins, secs


def printTime(mins: int, secs: int) -> str:
    """Print time to screen in format 00:00
    and also, returns string as variable
    >>> printTime(25, 00)
    25:00
    '25:00'
    """
    timer = "{:02d}:{:02d}".format(mins, secs)
    print(timer)
    return timer


def main():
    t = int(input("enter time in seconds: "))

    while t != 0:
        mins, secs = convertTime(t)
        printTime(mins, secs)
        t = updateTime(t)
    print("finished!")


if __name__ == "__main__":
    main()
