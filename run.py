#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox
from CONSTANTS import UI_CONSTANTS as CNST


def build_canvas(master):
    # Code to add widgets will go here...
    video_canvas = tk.Canvas(master, width=800, height=600, bg="blue")
    video_canvas.grid(row=1, column=1)
    build_tools(master)


def build_tools(master):
    tools_frame = tk.Frame(master, width=800, height=200, bg="green")
    tools_frame.grid(row=2, column=1)
    build_settings(tools_frame)
    build_playing_frame(tools_frame)
    build_labeling_frame(tools_frame)

def build_settings(tools_frame):
    settings_frame = tk.LabelFrame(tools_frame, text="Settings", bg="red", width=250, height=200)
    settings_frame.grid(row=1, column=1)

    load_video_button = tk.Button(settings_frame, text="Load Video")
    load_video_button.place(x=CNST.PAD.value, y=CNST.PAD.value, height=40, width=100)

    fps_label = tk.Label(settings_frame, text="Playing FPS:")
    fps_label.place(x=CNST.PAD.value, y=CNST.PAD.value * 2 + 40, height=40, width=100)

    fps_entry = tk.Entry(settings_frame, justify=tk.CENTER)
    fps_entry.place(x=CNST.PAD.value*2+100, y=CNST.PAD.value * 2 + 40, height=40, width=100)


def build_playing_frame(tools_frame):
    playing_frame = tk.LabelFrame(tools_frame, text="Play Controller", bg="white", width=300, height=200)
    playing_frame.grid(row=1, column=2)

    fps_label = tk.Label(playing_frame, text="Current Frame:")
    fps_label.place(x=CNST.PAD.value+50, y=CNST.PAD.value, height=40, width=100)

    current_frame_number_entry = tk.Entry(playing_frame, justify=tk.CENTER)
    current_frame_number_entry.place(x=160, y=CNST.PAD.value, width=70, height=40)

    backward_play_button = tk.Button(playing_frame, text="<<")
    backward_play_button.place(x=30, y=CNST.PAD.value*2+40, height=40, width=35)

    pause_button = tk.Button(playing_frame, text="||")
    pause_button.place(x=130, y=CNST.PAD.value*2+40, height=40, width=35)

    forward_play_button = tk.Button(playing_frame, text=">>")
    forward_play_button.place(x=230, y=CNST.PAD.value*2+40, height=40, width=35)

    step_back_button = tk.Button(playing_frame, text="<")
    step_back_button.place(x=30, y=CNST.PAD.value*3+2*40, height=40, width=35)

    step_size_entry = tk.Entry(playing_frame, justify=tk.CENTER)
    step_size_entry.place(x=110, y=CNST.PAD.value*3+2*40, width=70, height=40)

    step_forward_button = tk.Button(playing_frame, text=">")
    step_forward_button.place(x=230, y=CNST.PAD.value*3+2*40, height=40, width=35)



def build_labeling_frame(tools_frame):
    labeling_frame = tk.LabelFrame(tools_frame, text="Labeling Controller", bg="green", width=250, height=200)
    labeling_frame.grid(row=1, column=3)

    current_frame_number_entry = tk.Button(labeling_frame, justify=tk.CENTER, text="Action Start")
    current_frame_number_entry.place(x=75, y=CNST.PAD.value, width=100, height=40)



master = tk.Tk(className="Action recognition tool")
build_canvas(master)
master.mainloop()