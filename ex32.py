the_count=[[1,2],3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list

for number in the_count:
	print "This is count %r" % number

#same as above
for fruits in fruits:
	print "A fruits of type:%s" % fruits

#also we can go tthrough mixed lists too
#notice we have to use %r since we don't konw what's in it

for i in change:
	print "I got %r" % i

#we can alse build lists,first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Elements was: %d" % i
