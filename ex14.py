from sys import argv

script,user_name=argv

prompt='> '


print "Hi %s,I'm the %s script." % (user_name,script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes=raw_input(prompt)

print "Where do you live %s?" % user_name
lives=raw_input(prompt)

print """  
Alright,so you said %r about liking me.
NIce!You live in %r.
""" % (likes,lives)