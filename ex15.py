# -*- coding: utf-8 -*      
# 文件使用中文注释后，由于中文是非ASCII字符，所以必须加上面的语句
from sys import argv

script, filename = argv

txt = open(filename)     #读取文件并把文件返回到txt

print "Here's your file %r:" % filename
print txt.read(10)   #对文件执行read命令
print txt.readline()   #对文件读取整行，似乎是接着前面输出的内容继续输出的

txt.close()   #关闭文件

print "Type the filename again:"     
file_again = raw_input('>')     #另一种读取文件的方式，在程序中输入文件名

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
