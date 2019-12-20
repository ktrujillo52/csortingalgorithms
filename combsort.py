#!/usr/bin/python
#Comb sort

#Initialize data array
l = [ 'c', 'a', 'e', 'b' , 'd']
print l
#Iterate through list
for i in range(len(l)-1):
	for j in range((len(l)-1)-i):
		if (l[i] < l[i+j]):
			next
		elif (l[i] == l[i+j]):
			next
		else:
			temp = l[i]
			l[i] = l[i+j] 
			l[i+j] = temp
print l				
