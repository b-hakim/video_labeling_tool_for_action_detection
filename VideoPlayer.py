import tkinter as tk
from time import sleep

import PIL
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
import Utilities as utl
from CONSTANTS import PLAYING_MODE

class VideoPlayerControllerFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.current_frame_label = tk.Label(self, text="Current Frame:")
        self.current_frame_label.place(relx=0.2, rely=0.1, anchor=tk.CENTER,
                                       width=100, height=25)

        self.current_frame_number_entry = tk.Entry(self, justify=tk.CENTER)
        self.current_frame_number_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER, width=50, height=25)

        self.current_frame_number_entry.insert(tk.END, "30")

        self.backward_play_button = tk.Button(self, text="<<", command=self.backward_play_button_clicked)
        self.backward_play_button.place(relx=0.25, rely=0.3, anchor=tk.CENTER)

        self.pause_button = tk.Button(self, text="||", command=self.pause_button_clicked)
        self.pause_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.forward_play_button = tk.Button(self, text=">>", command=self.forward_play_button_clicked)
        self.forward_play_button.place(relx=0.75, rely=0.3, anchor=tk.CENTER)

        self.step_backward_button = tk.Button(self, text="<", command=self.step_backward_button_clicked)
        self.step_backward_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

        self.step_size_entry = tk.Entry(self, justify=tk.CENTER)
        self.step_size_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=50, height=25)
        self.step_size_entry.insert(tk.END, "1")

        self.step_forward_button = tk.Button(self, text=">", command=self.step_forward_button_clicked)
        self.step_forward_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

        self.playing_mode=PLAYING_MODE.PAUSED

    def step_forward_button_clicked(self):
        if self.playing_mode != PLAYING_MODE.PAUSED:
            messagebox.showinfo("Pause Video First", "Kindly Pause the video first")
            return

        cap = self.master.settings_frame.video_cap
        step = self.step_size_entry.get()
        canvas = self.master.master.master.master.canvas_frame.video_canvas

        if not step.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a correct stepping size")
            return

        current_frame = self.current_frame_number_entry.get()

        if not current_frame.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a specific Frame Index")
            return

        current_frame = int(current_frame)
        current_frame += int(step)

        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        has_frame, frame = cap.read()

        if has_frame:
            self.current_frame_number_entry.delete(0, tk.END)
            self.current_frame_number_entry.insert(0, current_frame)
            utl.update_canvas_from_cv_image(canvas, frame)

    def step_backward_button_clicked(self):
        if self.playing_mode != PLAYING_MODE.PAUSED:
            messagebox.showinfo("Pause Video First", "Kindly Pause the video first")
            return

        step = self.step_size_entry.get()
        cap = self.master.settings_frame.video_cap

        if cap is None:
            messagebox.showinfo("Error Loading Video", "Kindly select a video first")
            return

        if not step.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a correct stepping size")
            return

        current_frame = self.current_frame_number_entry.get()

        if not current_frame.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a specific Frame Index")
            return

        canvas = self.master.master.master.master.canvas_frame.video_canvas

        current_frame = int(current_frame)
        current_frame -= int(step)

        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        has_frame, frame = cap.read()

        if has_frame:
            self.current_frame_number_entry.delete(0, tk.END)
            self.current_frame_number_entry.insert(0, current_frame)
            utl.update_canvas_from_cv_image(canvas, frame)

    def forward_play_button_clicked(self):
        # Check if alreayd forward playing
        if self.playing_mode == PLAYING_MODE.FORWARD:
            return

        self.playing_mode=PLAYING_MODE.FORWARD
        cap = self.master.settings_frame.video_cap
        canvas = self.master.master.master.master.canvas_frame.video_canvas

        has_frame = True

        if cap is None:
            messagebox.showinfo("Error Loading Video", "Kindly select a video first")
            return

        current_frame = self.current_frame_number_entry.get()

        if not current_frame.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a specific Frame Index")
            return

        current_frame = int(current_frame)

        if int(current_frame) < 0:
            messagebox.showinfo("Error Loading Frame", "Kindly Select a correct Frame Index")
            return

        # Todo: change 200 to a variable in the settings section
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

        # todo: change batch_size to parameter in Settings
        # batch_size = 200
        # idx = current_frame
        # video_frames = []

        while has_frame:
            # if idx == len(video_frames) or len(video_frames) == 0:
            #     video_frames = utl.get_batch_from_video(cap, current_frame, current_frame+batch_size)
            #     idx = 0

            # if self.playing_mode != PLAYING_MODE.FORWARD or len(video_frames) == 0:
            #     return
            if self.playing_mode != PLAYING_MODE.FORWARD:
                return

            has_frame, frame = cap.read()

            if not has_frame:
                return

            # frame = video_frames[idx][:, :, ::-1]
            utl.update_canvas_from_cv_image(canvas, frame)

            self.current_frame_number_entry.delete(0, tk.END)
            current_frame += 1
            # idx += 1
            self.current_frame_number_entry.insert(0, current_frame)

            # sleep(0.005)  # 1/int(self.master.settings_frame.fps_entry.get()))

    def pause_button_clicked(self):
        self.playing_mode=PLAYING_MODE.PAUSED

    def backward_play_button_clicked(self):
        self.playing_mode=PLAYING_MODE.BACKWARD
        ret = True
        cap = self.master.settings_frame.video_cap
        canvas = self.master.master.master.master.canvas_frame.video_canvas

        if cap is None:
            messagebox.showinfo("Error Loading Video", "Kindly select a video first")
            return

        current_frame = self.current_frame_number_entry.get()

        if not current_frame.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a specific Frame Index")
            return

        current_frame = int(current_frame)

        if int(current_frame)<0:
            messagebox.showinfo("Error Loading Frame", "Kindly Select a correct Frame Index")
            return

        # Todo: change 200 to a variable in the settings section
        batch_size = 200
        start = current_frame - batch_size

        if start < 0:
            start = 0

        cap.set(cv2.CAP_PROP_POS_FRAMES, start)
        video_frames = utl.get_batch_from_video(cap, start, current_frame)

        current_frame = int(self.current_frame_number_entry.get())
        idx = len(video_frames)-1

        while ret:
            ch, cw = canvas.winfo_height(), canvas.winfo_width()

            if current_frame < 0 or not self.playing_mode == PLAYING_MODE.BACKWARD:
                return

            # todo: make it a parallel thread that runs before reaching the end by 50 frames
            if idx < 0:
                start = current_frame - batch_size

                if start < 0:
                    start = 0

                cap.set(cv2.CAP_PROP_POS_FRAMES, start)
                video_frames = utl.get_batch_from_video(cap, start, current_frame)
                idx = len(video_frames)-1

                if idx == -1:
                    return

            # has_frame, frame = cap.read()
            #
            # if not has_frame or current_frame == -1:
            #     return

            utl.update_canvas_from_cv_image(canvas, video_frames[idx])

            self.current_frame_number_entry.delete(0, tk.END)
            current_frame -= 1
            idx -= 1
            self.current_frame_number_entry.insert(0, current_frame)

            # sleep(0.005)#1/int(self.master.settings_frame.fps_entry.get()))

