#!/usr/bin/python
#Bubble sort

#Initialize data array
l = [ 'c', 'a', 'e', 'b' , 'd']
print l
#Iterate through list
for i in range(len(l)-1):
#	temp = l[i]
#	temp2 = l[i+1]
	if (l[i] < l[i+1]):
		next
	elif (l[i] == l[i+1]):
		next
	else:
#		l[i+1] = temp
#		l[i] = temp2
		temp = l[i]
		l[i] = l[i+1]
		l[i+1] = temp
print l				
