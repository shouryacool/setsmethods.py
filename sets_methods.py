# Creating An Empty Set
c =set()
print(c)

# Adding Value To empty Empty Set 
c.add(5)
# c.add([6,7]) # We Cannot Add List To Sets Bcs  List is  it is bcs we can change the contents of Lists Later unhashable  TypeError: unhashable type: 'list'

c.add((4,10,6))
 #But We can Add a Tuple 

print(c)

# UnHashable Data Types Cannot Be Added In Sets  (In Laymen Lang Unshable Means that its value can be changed Later on)
print(len(c)) #Returns 4, the length of the set
d={3,5,10,4}
d.remove(4)
print(d)
print(type(d))
print(d.pop())#Removes Random Value frpm set
