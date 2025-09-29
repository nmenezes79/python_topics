# Entry – Single Line Text Input

import tkinter as tk

root = tk.Tk()
root.title("Entry Example")

def show_text():
    user_text = entry.get()
    label.config(text=f"You typed: {user_text}")

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_text)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
