import os
import tkinter as tk
from tkinter import messagebox


class EditLabelsFrame(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        tk.LabelFrame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.remove_action_button = tk.Button(self, text="Remove Label", command=self.remove_action_button_clicked)
        self.remove_action_button.place(relx=0.25, rely=0.25, width=150, height=30)

        self.save_action_list_button = tk.Button(self, text="Save Label List",
                                                 command=self.save_action_list_button_clicked )
        self.save_action_list_button.place(relx=0.25, rely=0.45, width=150, height=30)
        self.saved = False

    def remove_action_button_clicked(self):
        actions_listbox = self.master.master.master.labeled_actions_frame.action_listbox
        selection = actions_listbox.curselection()

        if len(selection) == 0:
            return

        actions_listbox.delete(selection[0])

    def save_action_list_button_clicked(self):
        video_path = self.master.master.master.tools_frame.settings_frame.video_path
        file_name = os.path.basename(video_path)
        actions_listbox = self.master.master.master.labeled_actions_frame.action_listbox

        sorted_action_list = []
        for i, entry in enumerate(actions_listbox.get(0, tk.END)):
            action_id, action_name, start_frame_index, end_frame_index = entry.split(',')
            sorted_action_list.append([action_id.strip(), action_name.strip(), start_frame_index.strip(), end_frame_index.strip()])

        sorted_action_list.sort(key=lambda x: int(x[2]))

        with open(video_path.replace(file_name, file_name[:file_name.index('.')]+".txt"), 'w') as fw:
            for entry in sorted_action_list:
                action_id, action_name, start_frame_index, end_frame_index = entry
                fw.write("{},{},{}\n".format(action_id,
                                             start_frame_index,
                                             end_frame_index))

        messagebox.showinfo("Video Label saved successfully", "Video list has been saved successfully")
        self.saved=True