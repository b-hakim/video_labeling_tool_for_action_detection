import tkinter as tk


class SettingsController(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.settings_frame = tk.LabelFrame(master, text="Settings", bg="red", width=250, height=200)
        self.settings_frame.grid(row=1, column=1)

        self.load_video_button = tk.Button(self.settings_frame, text="Load Video")
        self.load_video_button.place(x=10, y=10, height=40, width=100)

        self.fps_label = tk.Label(self.settings_frame, text="Playing FPS:")
        self.fps_label.place(x=10, y=10 * 2 + 40, height=40, width=100)

        self.fps_entry = tk.Entry(self.settings_frame, justify=tk.CENTER)
        self.fps_entry.place(x=10*2+100, y=10 * 2 + 40, height=40, width=100)

