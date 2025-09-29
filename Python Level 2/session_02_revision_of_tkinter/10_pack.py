# pack() - Arranges Widgets Top, Bottom, Left, Right (Like Stacking Blocks).

import tkinter as tk

root = tk.Tk()
root.title("pack Example")

label1 = tk.Label(root, text="Top", bg="lightblue")
label1.pack(side="top", fill="x")

label2 = tk.Label(root, text="Left", bg="lightgreen")
label2.pack(side="left", fill="y")

label3 = tk.Label(root, text="Right", bg="lightpink")
label3.pack(side="right", fill="y")

label4 = tk.Label(root, text="Bottom", bg="lightyellow")
label4.pack(side="bottom", fill="x")

root.mainloop()
