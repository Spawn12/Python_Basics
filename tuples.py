#****************************** Tuples ***************************#
#Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

#Note: When compared with lists, tuples are simple data structures. Use them
#when you want to store a set of values that should not be changed throughout
#the life of a program.
my_list=(200,2.30,"Cat",False)
list=[]
print (my_list)
print(my_list[2])
#print (list[4])# it as an erro because its an out of range
#my_list.append("dog") # we cant append any element
#my_list[1]=244 # we cant change any element only we can acccess the element
for value in my_list:
    print(value)
    list.append(value)
print(list)
list.append(3) #we ca play the copy of tuples list
print(list)

#To overwrite the dimmension we have to redefine whole Dimension
print("\nOriginal my_list:")
for my_list in my_list:
    print(my_list)
    my_list = (400, 100)
print("\nModified my_list:")
for my_list in my_list:
    print(my_list)
