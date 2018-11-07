import tkinter as tk
from tkinter import filedialog
from SelectAction import ActionSelectionWindow


class LabelingControllerFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        # self.labeling_frame = tk.LabelFrame(self, text="Labeling Controller", bg="green", width=250, height=200)
        # self.labeling_frame.pack(side="right")

        self.master = master

        self.load_actions_button = tk.Button(self, justify=tk.CENTER, text="Load action list",
                                             command=self.load_actions_button_clicked)

        self.load_actions_button.place(relx=0.25, rely=0.05, width=150, height=30)

        self.action_start_button = tk.Button(self, justify=tk.CENTER, text="Action Start",
                                             command=self.action_start_button_clicked)
        self.action_start_button.place(relx=0.25, rely=0.25, width=150, height=30)

        self.action_end_button = tk.Button(self, justify=tk.CENTER, text="Action End",
                                           command=self.action_end_button_clicked)
        self.action_end_button.place(relx=0.25, rely=0.45, width=150, height=30)

        self.edit_started_actions_button = tk.Button(self, justify=tk.CENTER, text="Edit Started Actions",
                                           command=self.edit_started_actions_button_clicked)
        self.edit_started_actions_button.place(relx=0.25, rely=0.65, width=150, height=30)

        self.list_actions = []
        self.started_actions = []

    def edit_started_actions_button_clicked(self):
        print ("Not yet implemented")

    def action_end_button_clicked(self):
        started_action_list = []

        for id, class_name in self.list_actions:
            matches = list(filter(lambda x:int(x[0]) == id, self.started_actions))
            if  len(matches) > 0:
                started_action_list.extend(matches)

        self.master.playing_controller_frame.pause_button_clicked()
        ActionSelectionWindow(started_action_list, self.append_action_to_listbox)

    def append_action_to_listbox(self, action_details):
        ending_frame = self.master.playing_controller_frame.current_frame_number_entry.get()
        action_id, action_name, starting_frame = action_details.split(',')

        actions_listbox = self.master.master.master.master.labeled_actions_frame.action_listbox
        actions_listbox.insert(tk.END, ", ".join((action_id, action_name, starting_frame, ending_frame)))
        print("adding action to list box: " + action_name)

        for item in self.started_actions:
            if item[0] == action_id:
                self.started_actions.remove(item)
                break

    def action_start_button_clicked(self):
        self.master.playing_controller_frame.pause_button_clicked()
        ActionSelectionWindow(self.list_actions, self.add_to_started_list)

    def add_to_started_list(self, action_details):
        starting_frame_index = int(self.master.playing_controller_frame.current_frame_number_entry.get())
        action_id, action_name = action_details.split(',')
        self.started_actions.append([action_id, action_name, starting_frame_index])

    def load_actions_button_clicked(self):
        # filepath = filedialog.askopenfilename(initialdir="/", title="Select file",
        #                                       filetypes=(("Text files", "*.txt"), ("CSV files", "*.csv")))
        filepath="/home/bassel/data/office-actions/office_actions_19/class_index.txt"
        with open(filepath) as fw:
            for line in fw:
                id, name = line.split(',')
                self.list_actions.append((int(id), name))