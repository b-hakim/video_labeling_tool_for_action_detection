import tkinter as tk

import cv2

import Utilities as utl


class LabeledActionsFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.action_listbox = tk.Listbox(self)
        self.action_listbox.pack(fill="both", expand=True)

        self.action_listbox.bind("<Double-1>", self.action_listbox_double_clicked)

    def action_listbox_double_clicked(self, event):
        self.master.master.master.tools_frame.playing_controller_frame.pause_button_clicked()
        canvas = self.master.master.master.canvas_frame.video_canvas
        video_cap = self.master.master.master.tools_frame.settings_frame.video_cap
        current_frame_number_entry = self.master.master.master.\
                                                    tools_frame.playing_controller_frame.current_frame_number_entry
        selection = self.action_listbox.curselection()
        action_id, action_name, start, end = self.action_listbox.get(selection[0]).split(', ')
        start = int(start)
        video_cap.set(cv2.CAP_PROP_POS_FRAMES, start)
        has_frame, frame = video_cap.read()

        current_frame_number_entry.delete(0, tk.END)
        current_frame_number_entry.insert(0, start)

        utl.update_canvas_from_cv_image(canvas, frame)