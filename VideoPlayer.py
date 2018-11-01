import tkinter as tk


class VideoPlayerController(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.playing_frame = tk.LabelFrame(master, text="Play Controller", bg="white", width=300, height=200)
        self.playing_frame.grid(row=1, column=2)

        self.fps_label = tk.Label(self.playing_frame, text="Current Frame:")
        self.fps_label.place(x=10+50, y=10, height=40, width=100)

        self.current_frame_number_entry = tk.Entry(self.playing_frame, justify=tk.CENTER)
        self.current_frame_number_entry.place(x=160, y=10, width=70, height=40)

        self.backward_play_button = tk.Button(self.playing_frame, text="<<")
        self.backward_play_button.place(x=30, y=10*2+40, height=40, width=35)

        self.pause_button = tk.Button(self.playing_frame, text="||")
        self.pause_button.place(x=130, y=10*2+40, height=40, width=35)

        self.forward_play_button = tk.Button(self.playing_frame, text=">>")
        self.forward_play_button.place(x=230, y=10*2+40, height=40, width=35)

        self.step_back_button = tk.Button(self.playing_frame, text="<")
        self.step_back_button.place(x=30, y=10*3+2*40, height=40, width=35)

        self.step_size_entry = tk.Entry(self.playing_frame, justify=tk.CENTER)
        self.step_size_entry.place(x=110, y=10*3+2*40, width=70, height=40)

        self.step_forward_button = tk.Button(self.playing_frame, text=">")
        self.step_forward_button.place(x=230, y=10*3+2*40, height=40, width=35)



