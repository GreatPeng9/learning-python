from sys import argv

script, username = argv
prompt = ">"

print "hi %s,I'm the %s script." %(username, script)
print "I'd ask you some question"
print "do you like me, %s" % username
like = raw_input(prompt)

print "Where do you live, %s" %username
live = raw_input(prompt)

print "What computer do you have"
com = raw_input(prompt)

print """
Alright, so you said %s about me,
you live in %s,
and you have a %s computer.
""" %(like,live,com)
