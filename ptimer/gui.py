from functools import partial

from tkinter import Tk, Entry
from tkinter import ttk

from ptimer import start_countdown, pause_countdown


def set_timer(timer_textbox):
    """gets time variable and passes it to start_countdown"""
    t = timer_textbox.get()
    start_countdown(t)

def main():
    root = Tk()

    frame = ttk.Frame(root, padding=40)
    frame.grid()

    timer_textbox = Entry(frame, width=10, borderwidth=5)
    timer_textbox.grid(row=0, column=0, padx=10, pady=10)
    timer_textbox.insert(0, "00:00")

    ttk.Button(frame, text="Start", command=partial(set_timer, timer_textbox)).grid(column=0, row=1, padx=10)
    
    ttk.Button(frame, text="Pause", command=partial(pause_countdown, timer_textbox, timer_textbox)).grid(column=1, row=1, padx=10)
    
    root.mainloop()


if __name__ == "__main__":
    main()
