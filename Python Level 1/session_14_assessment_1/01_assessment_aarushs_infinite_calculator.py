import tkinter as tk
import math

# Function to update expression
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except Exception as e:
            display_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        display_var.set("")
    elif text == "√":
        try:
            result = str(math.sqrt(float(expression)))
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""
    elif text == "x²":
        try:
            result = str(float(expression) ** 2)
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""
    else:
        expression += text
        display_var.set(expression)

# Main GUI window
root = tk.Tk()
root.title("Aarush's Python Calculator")
root.geometry("350x500")
root.config(bg="#20232A")

expression = ""
display_var = tk.StringVar()

# Entry display
display = tk.Entry(root, textvar=display_var, font="Arial 24", bd=10, relief=tk.RIDGE, justify="right", bg="#61dafb")
display.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=20)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "x²", "√"]
]

# Create buttons in rows
for row in buttons:
    frame = tk.Frame(root, bg="#20232A")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.GROOVE, bg="#282c34", fg="white", activebackground="#61dafb")
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()
