# Text – Multi Line Text Input

import tkinter as tk

root = tk.Tk()
root.title("Text Example")

text = tk.Text(root, height=5, width=40)
text.pack()

def show_text():
    content = text.get("1.0", tk.END)  # From line 1, character 0 to the end
    label.config(text=content.strip())

button = tk.Button(root, text="Get Text", command=show_text)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
