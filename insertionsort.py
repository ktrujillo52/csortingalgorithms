#!/usr/bin/python
#Insertion sort
#Initialize data arrray
l = ['5', '3', '1', '2', '4', '6']
r= l[::-1]
#Iterate
for i,j in zip(l,r):
		if (i < j):
			temp = i
			i = j
			j = temp
		else:
			break

print l
print r
