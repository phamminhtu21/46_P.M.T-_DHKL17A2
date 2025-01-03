import tkinter as tk

root = tk.Tk()
root.title("Cửa sổ Tkinter với Nhãn")

label = tk.Label(root, text="Đây là một nhãn!")
label.pack()

root.mainloop()
