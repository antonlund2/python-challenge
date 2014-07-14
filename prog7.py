#!/usr/bin/env python

from PIL import Image


im = Image.open("oxygen.png")
im = im.convert("L")
w=im.size[0]
h=im.size[1]
s = ""
lastchar = s

pix = im.load()

for i in range((w-21)):
    char = chr(pix[i,46])
    if char is not lastchar:
        s += char
    lastchar = char

ind = s.find("[")
s = s[ind+1:len(s)-1]
intlist = map(int,s.split(','))
print s
s2 = ''
intlist2 = 105, 110, 116, 101, 103, 114, 105, 116, 121
for i in intlist2:
    s2 += chr(i)
print s2
