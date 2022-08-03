import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Pictures transformer")
window.geometry("900x600+100+100")
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

# selected image
selectimage = Frame(width=400, height=400, bg="#d6dee5")
selectimage.place(x=10, y=120)

f = Frame(selectimage, bg="black", width=380, height=320)
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

window.mainloop()