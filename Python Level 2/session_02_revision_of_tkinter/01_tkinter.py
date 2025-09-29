import tkinter as tk

# Create the Main Window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")  # Width x Height

# Add a Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Add a Button
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="You clicked the button!"))
button.pack()

# Run the GUI Loop
root.mainloop()
