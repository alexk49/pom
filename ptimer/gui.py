from functools import partial

from tkinter import Tk, Entry
from tkinter import ttk

from ptimer import start_countdown


def set_timer(timer_textbox):
    """gets time variable and passes it to start_countdown"""
    t = timer_textbox.get()
    start_countdown(t)

def main():
    root = Tk()

    frame = ttk.Frame(root, padding=40)
    frame.grid()
    
    timer_textbox = Entry(frame, width=10, borderwidth=5)
    timer_textbox.grid(row=0, column=0)
    timer_textbox.insert(0, "00:00")

    ttk.Button(frame, text="Start timer", command=partial(set_timer, timer_textbox)).grid(column=1, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=2)
    

    root.mainloop()


if __name__ == "__main__":
    main()
