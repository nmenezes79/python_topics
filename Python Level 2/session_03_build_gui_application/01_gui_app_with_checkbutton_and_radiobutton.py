import tkinter as tk
from tkinter import messagebox

class PicnicPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Picnic Planner")

        self.activities = {
            "Hiking": tk.BooleanVar(),
            "Frisbee": tk.BooleanVar(),
            "Music": tk.BooleanVar(),
            "Picnic": tk.BooleanVar(),
        }

        self.selected_activity = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Activities:").pack()

        for activity, var in self.activities.items():
            tk.Checkbutton(self.root, text=activity, variable=var).pack()

        tk.Label(self.root, text="Select Activity to Do:").pack()

        for activity in self.activities:
            tk.Radiobutton(self.root, text=activity, variable=self.selected_activity,
            value=activity).pack()

        tk.Button(self.root, text="Plan Picnic", command=self.plan_picnic).pack()

    def plan_picnic(self):
        selected_activities = [activity for activity, var in self.activities.items() if var.get()]
        if not selected_activities:
            messagebox.showerror("Error", "Please select at least one activity.")
            return

        chosen_activity = self.selected_activity.get()
        messagebox.showinfo("Picnic Planned", f"Activities: {', '.join(selected_activities)}"
                            f"\nChosen Activity: {chosen_activity}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PicnicPlanner(root)
    root.mainloop()
