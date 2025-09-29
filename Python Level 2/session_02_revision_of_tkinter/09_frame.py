# Frame – Container for Grouping Widgets

import tkinter as tk

root = tk.Tk()
root.title("Frame Example")

frame = tk.Frame(root, borderwidth=2, relief="groove")
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Inside Frame").pack()
tk.Button(frame, text="Button in Frame").pack()

root.mainloop()
