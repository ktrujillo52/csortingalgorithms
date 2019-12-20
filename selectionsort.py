#!/usr/bin/python
#Selection sort

#Initialize data array
l = [ 'c', 'a', 'e', 'b' , 'd']
print l
#Iterate through list
for i in range(len(l)-1): 
	for j in range(len(l)-1):
		if (l[i] <= l[j]):		#set minimum as i
			temp = l[i]
			l[i] = l[j]
			l[j] = temp
		else:
			next
print l				
