#!/bin/env python3
"""Attacker decision util"""
import tkinter as tk
import random

from playsound import playsound
from tkinter import ttk
import time


class DigitalClock(tk.Tk):
    """."""
    def __init__(self):
        super().__init__()

        self.count = 0
        # configure the root window
        self.title('Attacker decision')
        self.resizable(0, 0)
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.attributes('-fullscreen', True)
        self['bg'] = 'black'

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='red')

        # label
        self.label = ttk.Label(
            self,
            text=self.time_string(),
            font=('Digital-7', 15)
        )

        # label 2
        self.label_info = ttk.Label(
            self,
            text="Starting..",
            font=('Digital-7', 200)
        )

        # label 3
        self.label_count = ttk.Label(
            self,
            text=self.count,
            font=('Digital-7', 10)
        )

        self.label.pack(expand=True)
        self.label_info.pack(expand=True)
        self.label_count.pack(expand=True)

        # schedule an update every 1 second
        self.label.after(1000, self.update)
        self.label_info.after(5000, self.update_info)

    def play_signal(self):
        playsound('../res/apito.wav', False)

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def info_string(self):
        self.count += 1
        self.play_signal()
        return str(random.randint(1, 4))

    def update_info(self):
        self.label_info.configure(text=self.info_string())
        self.label_count.configure(text=self.count)

        # schedule another timer
        self.label_info.after(3000, self.update_info)

    def update(self):
        """ update the label every 1 second """
        self.label.configure(text=self.time_string())

        # schedule another timer
        self.label.after(1000, self.update)


if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()
