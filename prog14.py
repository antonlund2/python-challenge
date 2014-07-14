#!usr/bin/env python

import math
from PIL import Image

im = Image.open("wire.png")
im2 = Image.new(im.mode,(100,100))

#remember: 100*100 = (100+99+99+98) + (...

n = 0
for i in range(0,50,1):
    for j in range(i,100-i):
        im2.putpixel( (j,i) ,im.getpixel((n,0)))
        n+=1
    for j in range(i,100-i-1):
        im2.putpixel( (100-i-1,j) ,im.getpixel((n,0)))
        n+=1
    for j in range(i,100-i-1):
        im2.putpixel( (100-j-1,100-i-1) ,im.getpixel((n,0)))
        n+=1
    for j in range(i,100-i-2):
        im2.putpixel( (i,100-j-2) ,im.getpixel((n,0)))
        n+=1

#Good enough. Shows a cat!
im2.show()
