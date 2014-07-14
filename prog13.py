#!usr/bin/env python

import xmlrpclib

url = "http://www.pythonchallenge.com/pc/phonebook.php"
sp = xmlrpclib.ServerProxy(url)

print sp.system.listMethods()
print sp.system.methodHelp('phone')
print sp.phone('Bert')
