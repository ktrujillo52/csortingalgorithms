#!/usr/bin/python
#Brick sort
#Initialize data array
l = ['5', '3', '1', '2', '4']
print l
#Iterate
for i in range(0, len(l)-1, 2):
	if (l[i] > l[i+1]):
		temp = l[i]
		l[i] = l[i+1]
		l[i+1] = temp
	else:
		next
for j in range(1, len(l), 2):
	if (l[j] > l[j+1]):
		temp = l[j] 
		l[j] = l[j+1]
		l[j+1] = temp
	else:
		next
print l
