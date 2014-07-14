#!usr/bin/env python


import calendar


#Find year when 27th of January was thursday
print [ i for i in range(1506,2016,10) if calendar.weekday(i,1,1) ==3 ]
