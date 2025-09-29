# place() - Positions Widgets at Exact (x, y) Coordinates.

import tkinter as tk

root = tk.Tk()
root.title("place Example")
root.geometry("300x200")

tk.Label(root, text="Hello", bg="lightblue").place(x=50, y=50)
tk.Button(root, text="Click Me").place(x=150, y=100)

root.mainloop()
