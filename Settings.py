import tkinter as tk


class SettingsControllerFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.button_holder_frame = tk.Frame(self)
        self.load_video_button = tk.Button(self.button_holder_frame, text="Load Video")
        self.load_video_button.pack()
        self.button_holder_frame.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.fps_holder_frame = tk.Frame(self, pady=10)
        self.fps_label = tk.Label(self.fps_holder_frame, text="Playing FPS:")
        self.fps_label.pack(side=tk.LEFT, fill="both")

        self.fps_entry = tk.Entry(self.fps_holder_frame, justify=tk.CENTER)
        self.fps_entry.pack(side=tk.LEFT)
        self.fps_holder_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

