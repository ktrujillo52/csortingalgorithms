#!/usr/bin/python
#Random sort
#Initialize data array
from random import randint
#l = ['20', '17', '15', '9', '1', '16', '19', '12', '7', '3', '2', '4', '13', '11', '10', '6', '5', '8', '14', '18']
l = ['5', '3', '1', '2', '4', '6'] 
k = 0
sort = []
while (k == 0):
	count = 0
	sort = []
	numbers = []
	for i in l:
		y = randint(0,len(l)-1)
		numbers.append(y)
	newlist = []
	[newlist.append(number) for number in numbers if number not in newlist]	
	for i in newlist:		#build random array sort
		sort.append(l[i])

	for j in range(len(sort)-1):
		if (sort[j]<sort[j+1]):
			count = count + 1	
		else:
			break
	if (count == len(l)-1):
		print l
		print sort
		k = 1
	else:
		k = 0
	numbers = []
	newlist = []
	#with open("count.txt", "a+") as text:
	#	text.write(str(count)+"\n")
	#	text.close()


