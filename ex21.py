# -*- coding: UTF-8 -*-
def add(x,y):
	return x+y
	
def sub(x,y):
	return x-y 
	
def mul(x,y):
	return x*y 
	
def div(x,y):
	return x/y 
	
print "Please input\n 1.add\n 2.subtracting\n 3.multiplying\n 4.dividing\n"
num=int(raw_input())

print "Please input x and y"
x=int(raw_input("x: "))
y=int(raw_input('y: '))

if num == 1:
	print "The calculate out is %d" % add(x,y)
elif num == 2:
	print "The calculate out is %r" % sub(x,y)
elif num == 3:
	print "The calculate out is %r" % mul(x,y)
elif num == 4:
	print "The calculate out is %r" % div(x,y)