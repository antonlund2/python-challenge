#!/usr/bin/env python
#coding: utf-8
import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
i = ['83763']
tofind = "and the next nothing is "
max_iter = 400
count = 1
while count < 400:
    str= urllib.urlopen(url + i[0], proxies={}).read()
    print str
    if str.find(tofind)>-1:
        index = str.find(tofind)
        i = re.findall(r'\d+',str[index:])
    else:
        break
    count+=1
