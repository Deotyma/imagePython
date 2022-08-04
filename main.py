import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from PIL import ImageFilter
import os

window = Tk()
window.title("Pictures transformer")
window.geometry("900x600+100+100")
window.configure(bg="#e2f9b8")


def showimage():
    global filename
    global importedimage
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select image file", filetypes=(("PNG file", "*.png"),
                                                                                ("JPG file", "*.jpg"),
                                                                                ("JPEG file", "*.jpeg"),
                                                                                ("ALL file", "*.txt")))
    importedimage = Image.open(filename)
    importedimage = ImageTk.PhotoImage(importedimage)
    lbl.configure(image=importedimage, width=380, height=320)
    lbl.image = importedimage

def blurimage():
    image1 = Image.open(filename)
    bluredimage = image1.filter(ImageFilter.BLUR)
    bluredimage = ImageTk.PhotoImage(bluredimage)
    lbl.configure(image=bluredimage, width=380, height=320)
    lbl.image = bluredimage

def conturimage():
    image2 = Image.open(filename)
    conturedimage = image2.filter(ImageFilter.CONTOUR)
    conturedimage = ImageTk.PhotoImage(conturedimage)
    lbl.configure(image=conturedimage, width=380, height=320)
    lbl.image = conturedimage

def embossimage():
    image3 = Image.open(filename)
    embossedimage = image3.filter(ImageFilter.EMBOSS)
    embossedimage = ImageTk.PhotoImage(embossedimage)
    lbl.configure(image=embossedimage, width=380, height=320)
    lbl.image = embossedimage


def restartimage():
    lbl.configure(image=importedimage, width=380, height=320)
    lbl.image = importedimage

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
selectimage = Frame(width=400, height=400, bg="#939f5c")
selectimage.place(x=10, y=120)

f = Frame(selectimage, bg="black", width=380, height=320)
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

Button(selectimage, text="Select image", width=12, height=2, font="arial 14 bold", command=showimage).place(x=10, y=340)
Button(selectimage, text="Restart", width=12, height=2, font="arial 14 bold", command=restartimage).place(x=260, y=340)

# transformation section
# filter section
transformationsection = Frame(width=440, height=510, bg="#939f5c")
transformationsection.place(x=450, y=10)

Label(transformationsection, text="Filters:", font="arial 20 bold", fg="#fff", bg="#939f5c").place(x=10, y=10)

Button(transformationsection, text="BLUR", width=12, height=2, font="arial 14 bold", command=blurimage).place(x=10,
                                                                                                              y=50)
Button(transformationsection, text="CONTOUR", width=12, height=2, font="arial 14 bold", command=conturimage).place(x=155, y=50)
Button(transformationsection, text="EMBOSS", width=12, height=2, font="arial 14 bold", command=embossimage).place(x=300, y=50)


window.mainloop()
