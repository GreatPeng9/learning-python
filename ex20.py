# -*- coding: UTF-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)  #重新设置文件读取指针到开头
	
def print_a_line(line_count, f):
	print line_count, f.readline(),   #print自动输出一个\n   加逗号,可以避免
	
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line += 1    #  += 要连在一起
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

print current_file.readline()
current_file.seek(3,1)  #前一个代表偏移量，后一个代表0开头，1当前，2末尾
print current_file.readlines()