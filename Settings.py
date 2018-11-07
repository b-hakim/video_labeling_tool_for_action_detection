import os
import tkinter as tk
from tkinter import filedialog

import cv2

import Utilities as utl


class SettingsControllerFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.button_holder_frame = tk.Frame(self)
        self.load_video_button = tk.Button(self.button_holder_frame, text="Load Video",
                                           command=self.load_video_click)
        self.load_video_button.pack()
        self.button_holder_frame.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.fps_holder_frame = tk.Frame(self, pady=10)
        self.fps_label = tk.Label(self.fps_holder_frame, text="Playing FPS:")
        # self.fps_label.pack(side=tk.LEFT, fill="both")

        self.fps_entry = tk.Entry(self.fps_holder_frame, justify=tk.CENTER)
        self.fps_entry.pack(side=tk.LEFT)
        self.fps_entry.insert(0, "30")

        # self.fps_holder_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # self.rotation_holder_frame = tk.Frame(self, pady=10)
        # # self.rotation_180 =
        # self.rotation_holder_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.video_cap = None
        self.initial_dir = '/'

    def load_video_click(self):
        self.video_cap = None

        self.video_path = "/home/bassel/data/office-actions/raw_data/mobile/20181020_161703.mp4"

        self.video_path = filedialog.askopenfilename(initialdir=self.initial_dir, title="Select file",
                                              filetypes=(("Video files", "*.mp4"), ("all files", "*.*")))


        self.initial_dir = os.path.dirname(self.video_path)

        if self.video_path != "" and self.video_path != ():
            self.video_cap = cv2.VideoCapture(self.video_path)

        canvas = self.master.master.master.master.canvas_frame.video_canvas
        utl.update_canvas_from_cv_image(canvas, self.video_cap.read()[1])