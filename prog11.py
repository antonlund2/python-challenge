#!usr/bin/env python

from PIL import Image

im = Image.open("cave.jpg")
mode = "L"
im = im.convert(mode)
w=im.size[0]
h=im.size[1]

#Create new image. Set pixels to every  other pixel
im2 = Image.new(mode,(w/2,h/2))

for i in range(w/2):
    for j in range(h/2):
        im2.putpixel((i,j),im.getpixel((2*i+1,2*j+1)))
im2.show()
