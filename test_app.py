#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox
from CONSTANTS import UI_CONSTANTS as CNST
from CanvasFrame import CanvasFrame
from ToolsFrame import ToolsFrame



class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.canvas = CanvasFrame(self, bg="yellow")
        self.tools = ToolsFrame(self, bg="Black")

        self.canvas.pack(fill="y")
        # self.tools.pack(fill="both")


master = tk.Tk(className="Action recognition tool")
MainApplication(master).pack(side="top", fill="both", expand=True)
master.mainloop()