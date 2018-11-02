import tkinter as tk

import PIL
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox


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

        self.pause_button = tk.Button(self, text="||")
        self.pause_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.forward_play_button = tk.Button(self, text=">>")
        self.forward_play_button.place(relx=0.75, rely=0.3, anchor=tk.CENTER)

        self.step_back_button = tk.Button(self, text="<")
        self.step_back_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

        self.step_size_entry = tk.Entry(self, justify=tk.CENTER)
        self.step_size_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=50, height=25)

        self.step_forward_button = tk.Button(self, text=">")
        self.step_forward_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)


    def backward_play_button_clicked(self):
        ret = True
        vid_path = self.master.settings_frame.video_path
        current_frame = self.current_frame_number_entry.get()

        if vid_path == "":
            messagebox.showinfo("Error Loading Video", "Kindly Select a Video First")
            return
        elif not current_frame.isdigit():
            messagebox.showinfo("Error Loading Frame", "Kindly Select a specific Frame Index")
            return
        elif int(current_frame)<0:
            messagebox.showinfo("Error Loading Frame", "Kindly Select a correct Frame Index")
            return

        current_frame = int(current_frame)

        self.current_frame_number_entry.delete(0, tk.END)
        self.current_frame_number_entry.insert(0, current_frame-int(self.master.settings_frame.fps_entry.get()))

        cap = cv2.VideoCapture(vid_path)
        canvas = self.master.master.master.master.canvas_frame.video_canvas

        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        has_frame, frame = cap.read()

        if not has_frame:
            return

        # frame = cv2.resize(frame, (50, 50))
        print("working")
        frame = frame[:,:,::-1]
        photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = photo
        canvas.create_image(0, 0, image=photo, anchor="nw")

        if current_frame >= 0:
            self.master.after(int(self.master.settings_frame.fps_entry.get()), self.backward_play_button_clicked)