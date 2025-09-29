# Label – Display Text or Images

import tkinter as tk

root = tk.Tk()
root.title("Label Example")

label = tk.Label(root, text="This is a Label", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
