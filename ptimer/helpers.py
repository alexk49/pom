from tkinter import Entry


def update_timer_display(timer_textbox: Entry, t: str):
    """takes time as string variable: 00:00
    and sets timer textbox to given value"""
    timer_textbox.insert(0, t)
