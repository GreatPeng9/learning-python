
#print("hello world")
#print "hello world"
#print 'hello world'
#print "i'd much rather you 'not'."
#print 'i "said" do not touch this.\n'

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","tow","there","four")
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)

