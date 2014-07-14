#!usr/bin/env python

def lookandsay(n): #return next number in a lookandsay series
    list = [i for i in str(n)]
    count = 1
    last = ""
    res = ""
    for i in list:
        if i is last:
            count+=1
        else:
            if last is not "":
                res += str(count) + last
            last = i
            count=1
    res += str(count) + last
    return res

#look and say sequence
a = [1, 11, 21, 1211, 111221]
# len = [1, 2, 2, 4, 6]

start = 1
b = [start]
for i in range(30):
    n = lookandsay(b[len(b)-1])
    print str(i+1) + " length: " +str(len(str(n)))
    b.append(n)
