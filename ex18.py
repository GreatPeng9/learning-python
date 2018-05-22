# -*- coding: utf-8 -*  
def print_two(*args):  #定义函数
	arg1, arg2=args    #前面使用tab空格
	print "arg1: %r, arg2: %r" % (arg1,arg2)
	
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
def print_none():
	print "i got nothing."
	
	
print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("zed")
print_none