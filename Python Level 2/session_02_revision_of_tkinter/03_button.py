# Button – Perform an Action when Clicked

import tkinter as tk

root = tk.Tk()
root.title("Button Example")

def greet():
    label.config(text="Hello, Tkinter!")

label = tk.Label(root, text="Click the Button")
label.pack()

button = tk.Button(root, text="Click Me", command=greet)
button.pack()

root.mainloop()
