def validate_age():
    try:
        age = int(entry.get())
        if age >= 18:
            result_label.config(text="Bạn đủ tuổi để vào!")
        else:
            result_label.config(text="Bạn chưa đủ tuổi!")
    except ValueError:
        result_label.config(text="Hãy nhập tuổi hợp lệ!")

root = tk.Tk()
root.title("Age Validator")

tk.Label(root, text="Nhập tuổi của bạn:").pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Kiểm tra", command=validate_age)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
