import tkinter as tk
from Settings import SettingsController
from VideoPlayer import VideoPlayerController
from Labeling import LabelingController

class Tools(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.tools_frame = tk.Frame(master, width=800, height=200, bg="green")
        self.tools_frame.grid(row=2, column=1)

        self.settings = SettingsController(self.tools_frame)
        self.playing_controller = VideoPlayerController(self.tools_frame)
        self.labeling_controller = LabelingController(self.tools_frame)

