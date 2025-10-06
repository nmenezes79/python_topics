import calendar
import tkinter as tk
from tkinter import ttk
import datetime

# Function to display the calendar
def show_calendar():
    year = int(year_entry.get())
    month = int(month_combobox.get())
    cal_data = calendar.monthcalendar(year, month)

    # Clear any previous content
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    # Populate the days of the week with colored backgrounds
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        label = tk.Label(calendar_frame, text=day, padx=5, pady=5, relief="groove", bg="lightblue")
        label.grid(row=0, column=i+1)

    # Populate the calendar with colored backgrounds
    for week_num, week in enumerate(cal_data, start=1):
        for day_num, day in enumerate(week, start=1):
            if day != 0:
                bg_color = "lightgreen" if (day_num + week_num) % 2 == 0 else "lightyellow"
                label = tk.Label(calendar_frame, text=str(day), padx=5, pady=5, relief="groove", bg=bg_color)
                label.grid(row=week_num, column=day_num)

# Create the main window
root = tk.Tk()
root.title("Calendar")

# Year input
year_label = tk.Label(root, text="Year:")
year_label.grid(row=0, column=0)
current_year = datetime.datetime.now().year
year_entry = tk.Entry(root)
year_entry.insert(0, current_year)
year_entry.grid(row=0, column=1)

# Month input
month_label = tk.Label(root, text="Month:")
month_label.grid(row=1, column=0)
current_month = datetime.datetime.now().month
month_combobox = ttk.Combobox(root, values=list(range(1, 13)))
month_combobox.insert(0, current_month)
month_combobox.grid(row=1, column=1)

# Button to show calendar
show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.grid(row=2, columnspan=2)

# Frame to display calendar
calendar_frame = tk.Frame(root)
calendar_frame.grid(row=3, columnspan=2)

root.mainloop()
