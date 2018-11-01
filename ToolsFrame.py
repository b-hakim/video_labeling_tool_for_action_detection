import tkinter as tk
from Settings import SettingsControllerFrame
from VideoPlayer import VideoPlayerControllerFrame
from Labeling import LabelingControllerFrame


class ToolsFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.settings_frame = SettingsControllerFrame(self, bg="red", text="Video Player Settings", width=250, height=200)
        self.playing_controller_frame = VideoPlayerControllerFrame(self, bg="white",text="Video Player Controller", width=250, height=200)
        self.labeling_controller_frame = LabelingControllerFrame(self, bg="green", text="Labeling Controller", width=250, height=200)

        self.settings_frame.pack(fill="both", expand=True, side=tk.LEFT)
        self.playing_controller_frame.pack(fill="both", expand=True, side=tk.LEFT)
        self.labeling_controller_frame.pack(fill="both", expand=True, side=tk.LEFT)
