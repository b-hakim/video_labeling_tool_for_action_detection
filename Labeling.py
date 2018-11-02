import tkinter as tk


class LabelingControllerFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        # self.labeling_frame = tk.LabelFrame(self, text="Labeling Controller", bg="green", width=250, height=200)
        # self.labeling_frame.pack(side="right")

        self.master = master
        self.action_start_button = tk.Button(self, justify=tk.CENTER, text="Action Start")
        self.action_start_button.place(relx=0.25, rely=0.25, width=150, height=30)
