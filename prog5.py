#!/usr/bin/env python
#coding: utf-8

import pickle, pprint
data = pickle.load(open('banner.p', 'rb'))
str= ''
for line in data:
    for tuple in line:
        str += tuple[0] * tuple[1]
    str += '\n'
print(str)
