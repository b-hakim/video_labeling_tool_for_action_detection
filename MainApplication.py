#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox
from CanvasFrame import CanvasFrame
from EditLabeledActions import EditLabelsFrame
from LabeledActions import LabeledActionsFrame
from ToolsFrame import ToolsFrame


class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main_outline = tk.Frame(self)
        main_outline.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        main_outline.grid_columnconfigure(0, weight=3)
        main_outline.grid_columnconfigure(1, weight=1)
        main_outline.grid_rowconfigure(0, weight=3)
        main_outline.grid_rowconfigure(1, weight=1)

        top_left = tk.Frame(main_outline)
        top_left.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        top_right = tk.Frame(main_outline)
        top_right.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

        bottom_left = tk.Frame(main_outline)
        bottom_left.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)

        bottom_right = tk.Frame(main_outline)
        bottom_right.grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

        self.canvas_frame = CanvasFrame(top_left, bg="yellow")
        self.tools_frame = ToolsFrame(bottom_left, bg="Black")
        self.labeled_actions_frame = LabeledActionsFrame(top_right,
                                                         bg="orange", text="Action Labels")
        self.edit_labels = EditLabelsFrame(bottom_right, bg="yellow",
                                           text="Edit Labels", width=250, height=200)

        self.canvas_frame.pack(fill="both", expand=True)
        self.tools_frame.pack(fill="both", expand=True)
        self.labeled_actions_frame.pack(fill="both", expand=True)
        self.edit_labels.pack(fill="both", expand=True)

        # self.canvas_frame.grid(row=0, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        # self.tools_frame.grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
        # self.labeled_actions_frame.grid(column=1, sticky=tk.N+tk.E+tk.S+tk.W )


master = tk.Tk(className="Action recognition tool")
MainApplication(master).pack(fill="both", expand=True)
master.mainloop()