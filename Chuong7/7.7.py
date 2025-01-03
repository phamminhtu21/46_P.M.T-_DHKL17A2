import tkinter as tk

def calculate_sum():
    try:
        n = int(entry.get())
        result = sum(range(1, n + 1))
        result_label.config(text=f"The sum is: {result}")
    except ValueError:
        result_label.config(text="Please enter a valid integer!")

root = tk.Tk()
root.title("Sum Calculator")

tk.Label(root, text="Enter value of integer N:").pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Validate", command=calculate_sum)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
