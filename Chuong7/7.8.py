def calculate_divisors():
    try:
        n = int(entry.get())
        divisors = [str(i) for i in range(1, n + 1) if n % i == 0]
        result_label.config(text=f"The divisors of {n} are: {', '.join(divisors)}")
    except ValueError:
        result_label.config(text="Please enter a valid integer!")

root = tk.Tk()
root.title("Divisor Calculator")

tk.Label(root, text="Enter the value of N:").pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Validate", command=calculate_divisors)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
