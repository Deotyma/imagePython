from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

tulips = Image.open("./images/tulips.jpeg")
tulips.show()

# resize tulips
little = tulips.resize((128, 128))
little.show()

# rotate tulips
rotateImage = tulips.rotate(180)
rotateImage.show()

# all is black and white
im = tulips.convert("L")
im.show()

# change colors
r, g, b = tulips.split()
r = r.point(lambda i: i * 2)
g = g.point(lambda i: i / 2)
b = b.point(lambda i: i + 50)
img = Image.merge("RGB", (r, g, b))
img.getextrema()
img.show()

# Some filters
im1 = tulips.filter(ImageFilter.BLUR)
im1.show()

im2 = tulips.filter(ImageFilter.CONTOUR)
im2.show()

# contrast of 50%
contrastedImg = ImageEnhance.Contrast(tulips)
contrastedImg.enhance(1.5).show()


