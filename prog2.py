#!/usr/bin/env python
#coding: utf-8

import numpy

with open("text2") as myfile:
    data=list("".join(line.rstrip() for line in myfile))

print "".join([char for char in data if char.isalpha()])
