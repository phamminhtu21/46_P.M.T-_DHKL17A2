from math import gcd

def calculate():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        func = function_var.get()

        if func == "GCD":
            result = gcd(a, b)
            result_label.config(text=f"GCD({a}, {b}) = {result}")
        elif func == "LCM":
            lcm = abs(a * b) // gcd(a, b)
            result_label.config(text=f"LCM({a}, {b}) = {lcm}")
    except ValueError:
        result_label.config(text="Please enter valid integers!")

root = tk.Tk()
root.title("GCD and LCM Calculator")

tk.Label(root, text="Enter value of a:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter value of b:").pack()
entry2 = tk.Entry(root)
entry2.pack()

function_var = tk.StringVar(value="GCD")
tk.OptionMenu(root, function_var, "GCD", "LCM").pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
