#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox
from CONSTANTS import UI_CONSTANTS as CNST
from Tools import Tools


class Canvas(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        video_canvas = tk.Canvas(master, width=800, height=600, bg="blue")
        video_canvas.grid(row=1, column=1)

class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self)
        self.tools = Tools(self)



master = tk.Tk(className="Action recognition tool")
MainApplication(master).pack(side="top", fill="both", expand=True)
master.mainloop()