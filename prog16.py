#!usr/bin/env python

from PIL import Image
from PIL import ImageChops

image = Image.open("mozart.gif")
magic = chr(195)

for y in range(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bytes = row.tostring()
    i = bytes.index(magic)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)

image.save("new.gif")

image.show()
