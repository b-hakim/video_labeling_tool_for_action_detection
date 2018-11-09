import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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

        self.button_holder_frame = tk.Frame(self)
        self.load_labels_button = tk.Button(self.button_holder_frame, text="Load Video Labels",
                                           command=self.load_labels_click)
        self.load_labels_button.pack()
        self.button_holder_frame.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

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

    def load_labels_click(self):
        if self.video_path is not None:
            label_path = self.video_path.replace('.mp4', '.txt')

            if not os.path.isfile(label_path):
                messagebox.showerror("Unable to load labels", "This video does not have any labels")
                return

            actions_listbox = self.master.master.master.master.labeled_actions_frame.action_listbox

            with open(label_path) as fr:
                for line in fr:
                    aid, fstrart, fend = line.strip().split(',')
                    aname = self.get_aname(self.master.labeling_controller_frame.list_actions, int(aid))
                    actions_listbox.insert(tk.END, f"{aid}, {aname}, {fstrart}, {fend}")

    def get_aname(self, list_actions, aid):
        for action in list_actions:
            if int(action[0]) == aid:
                return action[1]

    def load_video_click(self):
        action_listbox = self.master.master.master.master.labeled_actions_frame.action_listbox

        if action_listbox.size() != 0:
            result = messagebox.askquestion("Load New Video", "Make sure you have already saved the action labels.\n"
                                                              "This list will be cleared when loading the new video\n"
                                                              "Are you sure to continue?", icon='warning')

            if result == "no":
                return

        self.video_cap = None

        # self.video_path = "/home/bassel/data/office-actions/raw_data/mobile/20181020_161703.mp4"

        self.video_path = filedialog.askopenfilename(initialdir=self.initial_dir, title="Select file",
                                              filetypes=(("Video files", "*.mp4"), ("all files", "*.*")))


        if self.video_path != "" and self.video_path != ():
            self.video_cap = cv2.VideoCapture(self.video_path)

            self.initial_dir = os.path.dirname(self.video_path)

            canvas = self.master.master.master.master.canvas_frame.video_canvas
            utl.update_canvas_from_cv_image(canvas, self.video_cap.read()[1])

            action_listbox.delete(0,tk.END)