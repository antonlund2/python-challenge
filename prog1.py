#!/usr/bin/env python
#coding: utf-8

import numpy
from string import maketrans

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


a = "abcdefghijklmnopqrstuvwxyz"
b = "cdefghijklmnopqrstuvwxyzab"
transtab = maketrans(a,b)
print(s.translate(transtab))
print("map".translate(transtab))
