import tkinter as tk


class VideoPlayerControllerFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        # self.playing_frame = tk.LabelFrame(master, text="Play Controller", bg="white", width=300, height=200)
        # self.playing_frame.grid(row=1, column=2)
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.current_frame_label = tk.Label(self, text="Current Frame:")
        self.current_frame_label.place(relx=0.2, rely=0.1, anchor=tk.CENTER, width=100, height=25)

        self.current_frame_number_entry = tk.Entry(self, justify=tk.CENTER)
        self.current_frame_number_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER, width=50, height=25)

        self.backward_play_button = tk.Button(self, text="<<")
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



