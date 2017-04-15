#***********************************List Manupalation**************************************#
#***************Basic Concept**************************************#
input_list = [2222, 4, 5, 17, 6, 9]
def func(list):
    new_list=list[:]
    for x in range(0,len(new_list)): #it will print the index of new_list
        print (x)
func(input_list)
def func(list): 
    new_list=list[:]
    for x in new_list: #it will print the element of new list
        print (x)
func(input_list)
#*******************************************************************#
x=["cat",2.5,500,True]
print(x)
x[1]="dog" # changing first element of x from 2.5 to dog
print(x)

bike=["honda","yamaha","suzuki"]
del bike[1] #deleting the value at index 1 from x
print(bike)

x=["cat",2.5,500,True]
x.insert(1,"dog")#its insert the element in given position
print(x)

x.append(False)#it will append the element at last
print(x)

y=x.pop(2)#it will pop that element out at given index and remove from that list If no index is specified , list.pop() removes the last item in the list
print(y+1)#you can also play with that pop out no
print("pop",x)

x.remove(False)#it will remove the given elment from the list
print(x)

list_one = [1, 2, 3, 4, 5, 6, 7]  # This is the first list
list_two = [10, 12, 14]           # This is the second list
list_one.extend(list_two)         # Extend list_one by appending all items of list_two
print(list_one)

my_list = [2, 3, 5, 7, 11, 13] # Create a list
my_list.clear()                # Remove all the items from the list
print(my_list) 

my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]# Create a list
my_index = my_list.index("is")                                # Return the index of the first "is"
print("The item was first found at index:", my_index)

my_list = ["mew", "mew", "kitten", "mew", "mew"]                  # Create a list
my_count = my_list.count("mew")                                   # Return the number of times "mew" appears
print("The number of times the item appeared was:", my_count)

my_list = ["zero", "one", "two", "three", "four", "five"]        # Create a list
my_list.reverse()                                                # Reverse the items of the list in place
print("Reversed list looks like:", my_list)

my_list.sort(reverse=True)                             #it will sort list in descending order
print(my_list)

my_list.sort()                             #it will sort list in ascending order
print(my_list)

original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()                     # Copy the original list and return it.        
print("Copied list looks like:", copied_list)

my_list = ['two', 5, ['one', 2]]
print(len(my_list))


my_list = [5, 3, 6, 1, 2, 4, 7]                  # Create a list
sorted(my_list, reverse=True)             # Sorted the items of the list in sort the item permenantlyorder
print("Sorted list looks like:", my_list)

my_list=['a','g','d','f','t','x','l']
my_list.sort()
print(my_list)


#*********************Multiple of no in list***************************#
def func(k,m):
    list=[]
    y=0
    for x in range (1,m+1):
        y=k*x
        list.append(y)
    list.sort(key=None, reverse=True) #sorting the list in reverse order
    return list
a=int(input("Enter no for multiple : "))
b=int(input("No of multiple : "))
print(func(a,b))


#***********************Append Even no in list ************************#
def func(a,b):
    list=[]
    y=0
    for x in range(a,b):
        if x%2==0:
            y=y+x
            list.append(x)
    return list,"Sum of all no in list : ",y
    
print(func(3,20))

#***********descending sorted list of cube root values of all the numbers from 1 to k***********#
def func(k):
    y=0
    list=[]
    if k==1:
        return False
    else:
        for x in range(1,k+1):
            y=pow(x,(1/3))              #pow is mathematical func which give x^y x to the power y pow(x,y) 
            list.append(y)
    list.sort(key=None, reverse=True)
    return list
print(func(5))

#*********************Divisor List of all no of k***************************#
def func(k):
    list=[]
    for x in range(1,k+1):
       if k%x==0:
           list.append(x)
    return list
print(func(20))

original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()                     # Copy the original list and return it.
copied_list.insert(1,10)
copied_list.remove("two")
print("Copied list looks like:", copied_list)

#******************* Creating list with range func *****************#
x=list(range(1,11)) #creating list from 1 to 10
print (x)
print(x[2])

x=list(range(1,11,2)) #creating list from 1 to 11 by skiping 2 (odd no)
print(x)

x=list(range(2,11,2)) ##creating list from 2 to 11 by skiping 2 (even no)
print(x)

a=[]
b=0
for value in range(1,11):
    #b=value**2
    a.append(value**2) #does the same work as up
print(a)

print (min(a)) #print the min number in list a
print (max(a)) #print max no in list a
print (sum(a)) #print sum of all the no in list a

#******************** List Comprehension **************************#
my_list=[ x**2 for x in range (1,11) ]
print (my_list)


def func(k):
    list=[]
    x=0
    for y in range(1,k):
        print("value of y :",y)
        if k%y==0:
            x=x+y
            list.append(y)
    print("Sum of divisors of k :",x)
    return list
print("list of Divisor of k :",func(18))
