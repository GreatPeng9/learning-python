# -*- coding: UTF-8 -*-
the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

for num in the_count:
	print ("this is count %d") % num
	
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
for i in change:
	print "I have got %r" % i
	
elements=[]

for i in range(0,6):
	print "adding %d to the list." % i
	elements.append(i)   #用于在列表末尾添加新的对象i
	
for i in elements:
	print "elements was: %d" % i