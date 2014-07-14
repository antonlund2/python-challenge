#!/usr/bin/env python
#coding: utf-8

import numpy
import string

with open("text3") as myfile:
    data=list("".join(line.rstrip() for line in myfile))

word = ""
linkedlist = [""] * 9

for c in data:
    del linkedlist[0]
    linkedlist.append(c)
    if \
        not linkedlist[0].isupper() and\
            linkedlist[1].isupper() and\
            linkedlist[2].isupper() and\
            linkedlist[3].isupper() and\
            linkedlist[4].islower() and\
            linkedlist[5].isupper() and\
            linkedlist[6].isupper() and\
            linkedlist[7].isupper() and\
        not linkedlist[8].isupper() \
        :
            word  += linkedlist[4]

print word
