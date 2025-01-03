from tkinter import Tk, Label, Entry, Button, StringVar

def reverse_word():
    word = input_var.get()
    reversed_word = word[::-1]
    result_var.set(reversed_word)

window = Tk()
window.title("Đảo ngược từ")

input_var = StringVar()
result_var = StringVar()

Label(window, text="Enter a word:").grid(row=0, column=0)
Entry(window, textvariable=input_var).grid(row=0, column=1)
Button(window, text="Validate", command=reverse_word).grid(row=1, column=0, columnspan=2)
Label(window, textvariable=result_var).grid(row=2, column=0, columnspan=2)

window.mainloop()