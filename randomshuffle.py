#!/usr/bin/python
from random import randint
#Random shuffle
#Initialize data array
l = ['5', '3', '1', '2', '4']
print l
#Iterate
for i in range(len(l)):
	y = randint(0, len(l)-1)
	temp = l[i]
	l[i] = l[y]		#swap iterable with random element
	l[y] = temp
print l
