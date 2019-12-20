#!/usr/bin/python
#Shell sort

#Initialize data array
l = [ 'c', 'a', 'e', 'b' , 'd']
print l
#Iterate through list
for i in range(len(l)-2):
	#Find minimum
	a = l[i]
	b = l[i+1]
	c = l[i+2]
	if (l[i] <= l[i+1] and l[i+1] <= l[i+2]):
		next
	elif (l[i] <= l[i+1] and l[i+1] >= l[i+2]):
		temp = l[i+2]
		l[i+2] = l[i+1]
		l[i+1] = temp
	elif (l[i] >= l[i+1] and l[i+1] <= l[i+2]):
		temp = l[i+1]
		l[i+1] = l[i]
		l[i] = temp
	elif (l[i] >= l[i+1] and l[i+1] >= l[i+2]):
		temp = l[i+1]
		l[i+1] = l[i]
		l[i] = temp
print l
