import tkinter as tk

def submit():
    print("Thông tin đã gửi!")

root = tk.Tk()
root.title("Nhập thông tin sinh viên")

tk.Label(root, text="Tên sinh viên:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="ID sinh viên:").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Mật khẩu:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Gửi", command=submit)
submit_button.pack()

root.mainloop()
