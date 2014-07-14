#!/usr/bin/env python
#coding: utf-8

import re

i = ['90052']
tofind = "Next nothing is "
max_iter = 400
count = 1
dir = 'channel/'
filelist = [i[0]]
while True:
    file = open(dir + i[0] + '.txt')
    lines = file.readlines()
    file.close()
    str = lines[0]


    if str.find(tofind)>-1:
        index = str.find(tofind)
        i = re.findall(r'\d+',str[index:])
        filelist.append(i[0])
    else:
        break

#Reading the zip-file comment
import zipfile
commentlist = []
z = zipfile.ZipFile('channel.zip',"r")
for file in z.infolist():
    filename = file.filename
    commentlist.append([filename[:filename.index('.')] , file.comment])


#Definitely not fastest way to find matches but works!
s = ''
for f1 in filelist:
    for f2 in commentlist:
        if f1 == f2[0]:
            s += f2[1]
            break

print s
