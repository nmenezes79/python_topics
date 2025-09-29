# Checkbutton – On/Off Option

import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")

var = tk.BooleanVar()

check = tk.Checkbutton(root, text="I agree", variable=var)
check.pack()

def submit():
    label.config(text=f"Agreed: {var.get()}")

button = tk.Button(root, text="Submit", command=submit)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
