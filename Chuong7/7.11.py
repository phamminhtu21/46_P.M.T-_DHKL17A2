import tkinter as tk
from datetime import datetime
import calendar

def show_date():
    date = datetime.now()
    lunar_date = calendar.TextCalendar().formatmonth(date.year, date.month)
    result_label.config(text=f"Dương lịch: {date.strftime('%Y-%m-%d %H:%M:%S')}\n\nLịch âm:\n{lunar_date}")

root = tk.Tk()
root.title("Date Display")

button = tk.Button(root, text="Hiển thị ngày", command=show_date)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
