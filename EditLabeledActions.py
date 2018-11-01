import tkinter as tk


class EditLabelsFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.remove_button = tk.Button(self, text="Remove Label")
        self.remove_button.place(relx=0.25, rely=0.25, width=150, height=30)