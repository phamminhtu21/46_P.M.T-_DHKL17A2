from tkinter import Tk, Label
from PIL import Image, ImageTk

def display_image(file_path):
    # Tạo cửa sổ Tkinter
    window = Tk()
    window.title("Chương trình xem ảnh")
    
    # Mở và hiển thị ảnh
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    
    label = Label(window, image=photo)
    label.pack()
    
    window.mainloop()

# Gọi hàm để hiển thị ảnh
display_image("Otto.png")



import requests
from io import BytesIO

def display_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(image)
    
    window = Tk()
    window.title("Chương trình xem ảnh")
    label = Label(window, image=photo)
    label.pack()
    window.mainloop()

# Gọi hàm
display_image_from_url("https://example.com/image.jpg")