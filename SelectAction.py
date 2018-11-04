import tkinter as tk

class ActionSelectionWindow(tk.Frame):
    def __init__(self, all_actions, update_output, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        master = tk.Toplevel(self)
        master.wm_title("Action Selection")

        self.label = tk.Label(master, text="Select an Action From List")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=100)

        self.action_listbox = tk.Listbox(master, height=30)
        self.action_listbox.pack(fill="both", expand=True)

        for item in all_actions:
            item = list(map(lambda x: str(x), item))
            self.action_listbox.insert(int(item[0]) - 1, ", ".join(item).strip())

        self.action_listbox.bind('<Double-1>', self.action_listbox_clicked)

        self.selected_action_id = None
        self.post_processing = update_output
        # self.action_listbox.bind('<<ListboxSelect>>', CurSelet)

    def action_listbox_clicked(self, event):
        # self.started_actions.append(self.action_listbox.curselection()[0]+1)
        id = self.action_listbox.curselection()[0]
        row = self.action_listbox.get(int(id))
        self.post_processing(row)

        event.widget.master.destroy()