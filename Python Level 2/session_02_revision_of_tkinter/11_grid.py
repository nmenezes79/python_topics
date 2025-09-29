# grid() - Arranges Widgets in a Table (Rows and Columns).

import tkinter as tk

root = tk.Tk()
root.title("grid Example")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root).grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Submit").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
