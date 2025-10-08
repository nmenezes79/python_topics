# 03_inclass_challenge_login_app.py

from tkinter import *
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")
frame.pack(pady=20)

# Add widgets
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=12)

name_entry = Entry(frame, bg="#BEBEBE", fg="black")
email_entry = Entry(frame, bg="#BEBEBE", fg="black")
pass_entry = Entry(frame, show="*", bg="#BEBEBE", fg="black")

textbox = Text(root, bg="#BEBEBE", fg="black", height=5, width=40)

def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

btn = Button(root, text="Create Account", command=display, bg="red", fg="white")

# Arrange all widgets
lbl1.grid(row=0, column=0, padx=10, pady=5)
name_entry.grid(row=0, column=1, padx=10, pady=5)
lbl2.grid(row=1, column=0, padx=10, pady=5)
email_entry.grid(row=1, column=1, padx=10, pady=5)
lbl3.grid(row=2, column=0, padx=10, pady=5)
pass_entry.grid(row=2, column=1, padx=10, pady=5)
btn.pack(pady=10)
textbox.pack(pady=10)

root.mainloop()
