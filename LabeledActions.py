import tkinter as tk


class LabeledActionsFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill="both", expand=True)
