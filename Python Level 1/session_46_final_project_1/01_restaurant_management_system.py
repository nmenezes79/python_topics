import tkinter as tk
from tkinter import messagebox
import time
import random

# Function to update time
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    time_label.config(text="Local Time: " + current_time)
    root.after(1000, update_time)  # update every second

# Function to generate random order number with selected items
def generate_order():
    selected_items = []
    total_price = 0

    if var_pizza.get() == 1:
        selected_items.append("Pizza")
        total_price += 250
    if var_burger.get() == 1:
        selected_items.append("Burger")
        total_price += 150
    if var_pasta.get() == 1:
        selected_items.append("Pasta")
        total_price += 200
    if var_coffee.get() == 1:
        selected_items.append("Coffee")
        total_price += 100

    if not selected_items:
        messagebox.showwarning("No Selection", "Please select at least one item!")
        return

    order_num = random.randint(1000, 9999)
    items_str = ", ".join(selected_items)
    messagebox.showinfo("Order Confirmed",
                        f"Order Number: {order_num}\nItems: {items_str}\nTotal: ₹{total_price}")

# Main window
root = tk.Tk()
root.title("Anusha's Restaurant")
root.geometry("450x400")

# Heading
heading = tk.Label(root, text="🍴 Welcome to Anusha's Restaurant 🍴", 
                font=("Arial", 14, "bold"), fg="darkgreen")
heading.pack(pady=10)

# Local time
time_label = tk.Label(root, text="", font=("Arial", 12))
time_label.pack()
update_time()

# Menu Section
menu_label = tk.Label(root, text="Menu (Select your items):", font=("Arial", 13, "underline"))
menu_label.pack(pady=10)

# Checkbuttons for menu
var_pizza = tk.IntVar()
var_burger = tk.IntVar()
var_pasta = tk.IntVar()
var_coffee = tk.IntVar()

cb1 = tk.Checkbutton(root, text="Pizza - ₹250", variable=var_pizza, font=("Arial", 12))
cb1.pack(anchor="w", padx=100)

cb2 = tk.Checkbutton(root, text="Burger - ₹150", variable=var_burger, font=("Arial", 12))
cb2.pack(anchor="w", padx=100)

cb3 = tk.Checkbutton(root, text="Pasta - ₹200", variable=var_pasta, font=("Arial", 12))
cb3.pack(anchor="w", padx=100)

cb4 = tk.Checkbutton(root, text="Coffee - ₹100", variable=var_coffee, font=("Arial", 12))
cb4.pack(anchor="w", padx=100)

# Buttons
order_btn = tk.Button(root, text="Place Order", font=("Arial", 12), bg="lightgreen",
                    command=generate_order)
order_btn.pack(pady=15)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), bg="lightcoral", command=root.quit)
exit_btn.pack(pady=5)

root.mainloop()
