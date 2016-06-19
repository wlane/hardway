from sys import argv

script,filename=argv

print "We're going to erase %r." % filename
print "If you don't want that,hot CTRL-C(^c)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target=open(filename,'a')

print "Truncating the file.Goodbye"
#target.truncate()

print "Now I'm going to ask you for these lines."

line1=raw_input("line1:")
line2=raw_input("line2:")

print "I'm going to write these to the file"

target.write(line1+"\n"+line2+"\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")

print "And finally we close it."
target.close()
