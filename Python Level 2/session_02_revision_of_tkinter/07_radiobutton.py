# Radiobutton – Choose One Option

import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")

choice = tk.StringVar(value="None")

tk.Radiobutton(root, text="Option A", variable=choice, value="A").pack()
tk.Radiobutton(root, text="Option B", variable=choice, value="B").pack()
tk.Radiobutton(root, text="Option C", variable=choice, value="C").pack()

def show_choice():
    label.config(text=f"Selected: {choice.get()}")

button = tk.Button(root, text="Submit", command=show_choice)
button.pack()

label = tk.Label(root, text="Selected: None")
label.pack()

root.mainloop()
