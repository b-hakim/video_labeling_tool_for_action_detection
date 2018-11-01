import tkinter as tk


class LabelingController(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.labeling_frame = tk.LabelFrame(master, text="Labeling Controller", bg="green", width=250, height=200)
        self.labeling_frame.grid(row=1, column=3)

        self.current_frame_number_entry = tk.Button(self.labeling_frame, justify=tk.CENTER, text="Action Start")
        self.current_frame_number_entry.place(x=75, y=10, width=100, height=40)
