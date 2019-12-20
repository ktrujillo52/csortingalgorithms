#!/usr/bin/python
#Quick sort

#Initialize data array
l = [ 'c', 'a', 'e', 'b' , 'd']
print l
#Iterate through list
middle = len(l) / 2
middle = round(middle) #round(middle,1)


k = 0
while (k == 0):
	middle = len(l) / 2
	middle = round(middle)
	count = 0
	n = []
	for i in range(len(l)):
		if (l[i] <= l[int(middle)]):
			n.insert(0,l[i])
		else:
			n.append(l[i])
	for i in range(len(n)-1):
		if (n[i] <= n[i+1]):
			count = count + 1
		else:
			break
	if (count == len(n)-1):
		k = 1
	else:
		k = 0
		l = n		
print n
