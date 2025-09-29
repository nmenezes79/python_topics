# Listbox – List of Items

import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")

listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack()

def show_selection():
    selection = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selection}")

button = tk.Button(root, text="Select", command=show_selection)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
