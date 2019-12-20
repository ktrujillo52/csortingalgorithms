#!/usr/bin/python
from random import randint
#Bogosort
#Initialize data array
l = ['5', '3', '1', '2', '4']
print l
#Iterate
for i in range(len(l)):
	y = randint(0, len(l)-1)
	z = randint(0, len(l)-1)
	temp = l[y]
	l[y] = l[z]		#shuffle random elements
	l[z] = temp
print l
