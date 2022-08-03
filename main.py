import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Pictures transformer")
window.geometry("900x500+100+100")
window.configure(bg="#e2f9b8")

# icon
image_icon = ImageTk.PhotoImage(file="images/tulips.jpeg")
window.iconphoto(False, image_icon)

# logo
image = Image.open("./images/tulips.jpeg")
img1 = image.resize((70, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(img1)
Label(image=logo, bg="#fff").place(x=10, y=10)

Label(text="Pictures transformer", font="arial 30 bold", fg="#313715", bg="#e2f9b8").place(x=90, y=50)

window.mainloop()