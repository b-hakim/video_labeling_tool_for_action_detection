import tkinter as tk


class CanvasFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)
        self.video_canvas = tk.Canvas(self, bg="blue")
        self.video_canvas.pack(expand=True, fill="both")