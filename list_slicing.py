#****************************************List Slicing*********************************#
list=["cat",25.2,65,True]
list[1]="lion" #replace the element at the given index
print(list)

#***********slicing**********#
#Note=we always give +1 index
a=list[1:3] #it will get the element from 1 to 2 index
print(a)
#***********************Returning ever skip next element*********************#
z=["we", "love", "python", "so","much"]
list=[]
list.append(z[0])
for x in range(1, len(z)):
    if x % 2 == 0:
        list.append(z[x])
        #print(element)
print(list)

#************Function Returning ever skip next element*******************#
def _every_other_element_sample_(sample_list):
    output = []
    length = len(sample_list)
    output.append(sample_list[0])
    for element in range(1, length):
        if element % 2 == 0:
            output.append(sample_list[element])
    return output
print(_every_other_element_sample_(z))

#***********************List Slicing with steps******************************#
list=["cat",2.5,600,"eagle",'elephant',True]
my_list=list[0:5:2] #[start index:end index:step] #it will slice from 0 to 4 index element and then slice to skiping every single element
print(my_list)
my_list=list[0:6:3] #it will slice from 0 to 5 index element and then slice to skiping every second element
print(my_list)

my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[0:6:2])

my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[0:6:1])

my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[6:0:-2])

my_list=['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[0:-1:3])

my_list=['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[-1:0:-1])

#**************************Default Indexing******************************#
#[:end index:step] if the start index is missing pyhthon assumed it 0
#[start:step] if the end index is missing pyhthon assumed it to all the way to end element including it
#[start:end index] if the step is missing pyhthon assumed it 1
my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
print(my_list[:3])

my_list=[24 ,'car', 'tv', 5.3, 'apple', 36]
print(my_list[2:])

my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
print(my_list[1:3:])

my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
print(my_list[2::3])

my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
print(my_list[::2])

my_list=[24, 'car', 'tv', 5.3, 'apple', 36]
print(my_list[::])

#********************Negative Indexing Slicing*********************************#
my_list=[54,'cow',0.25,32,'worm']
print(my_list[0:-2])

my_list=[54,'cow',0.25,32,'worm']
print(my_list[2:-2])

my_list=[54,'cow',0.25,32,'worm']
print(my_list[3:-3])

my_list=[54,'cow',0.25,32,'worm']
print(my_list[0:-1])

#***************************Assignment***************************#
#**********replacing the element with the given element and index***********************#
def func(a,replace):
    for x in range(1,4):
        a.pop(x)
        a.insert(x,replace)
    return a
x=['python', 3.4, 54, 'java', 82, 'c', 7.4]
y=(input("enter any thing to replace :"))
print(func(x,y))


#*******************Adding one element into another in a new list********************#
def func(A,B):
    new_list=A
    for x in B:
        new_list.append(x)
    return new_list
a=["safasf",32.5,33]
b=[60,True]
print(a)
print(b)
print(func(a,b))

#***********no no no******** Sorting list in asscending order without using builtin func********************************#
# Type your code here
def func(list):
    new_list=[]
    y=0
    for x in list:
        if x>y:
            y=x
            if x<y:
                new_list.append(x)
    return new_list
x=[65,88,2,95,-2,1,6]
print(len(x))

#********************Function that accepts a list and a value of an element and returns the count of how many times that element appears in the list.**************************************#
x=[32,"asdasd",5,65,"dasdasd",5]
def func(list,value):
    value_list=[]
    y=0
    for x in list:
        if x==value:
            value_list.append(x)
    return (len(value_list))
    
print("This value is ",func(x,5)," time in list")

#*************************list which contains all but the first and last elements of the original list.***************************#
def func(list):
    new_list=list[1:-1]
    return new_list
print(func(x))

#************Adding 1 to a new list except first and last one************************#
input_list = [2222, 4, 5, 17, 6, 9]
def func(list):
    new_list=list.copy()
    m=len(new_list)-1
    for x in range(1,m):
        a=new_list.pop(x)
        b=a+1
        new_list.insert(x,b)
    return new_list
print(func(input_list))

#**************************New list of all even no************************#
input_list = [2222, 4, 5, 17, 6, 9]
#Method 1
def func(list):
    new_list=list.copy()
    #input_list = my_list[:] #we can also copy element of list by this method
    for x in range(0,len(new_list)):
        if new_list[x]%2 !=0:
            a=new_list.pop(x)
            b=a+1
            new_list.insert(x,b)
    return new_list
print(func(input_list))

#Method 2
def _list_manipulation_sample5_(my_list):
    input_list = my_list[:]
    for x in range(0, len(input_list)):
        if input_list[x] % 2 != 0:
            input_list[x] = input_list[x] + 1
    return input_list
print(func(input_list))
#***************Basic Concept**************************************#
input_list = [2222, 4, 5, 17, 6, 9]
def func(list):
    new_list=list[:]
    for x in range(0,len(new_list)): #it will print the index of new_list
        print (x)
func(input_list)
def func(list): 
    new_list=list[:]
    for x in new_list: #it will print the element
        print (x)
func(input_list)

#****************************Sm of all no of 2 list******************************#
def func(a,b):
    y=0
    a.extend(b)
    for x in a:
        if x%2==0:
            y=y+x
    return y
x=[2222, 4, 5, 17, 6, 9]
y=[2,192,5,88,65]

print(func(x,y))

#********************Reverse of all the element in new list*******************************#
input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']
def func(list):
    #a=(-1*(len(list)+1))
    new_list=list[-1::-1]
    return new_list
print(func(input_list))

#**************************Create new list which dont have repetation**********************#
def unique_list(sample_list):
    output_list = []
    for items in sample_list:
        if items not in output_list:
            output_list.append(items)
    return output_list
print(unique_list(input_list))

#**************Create new list which dont have repetation in both list*************************#
y=['apples', 'eat', "don't", 'I']
def func(a,b):
    my_list=[]
    a.extend(b)
    for x in a:
        if x not in my_list:
            my_list.append(x)
    return my_list
print (func(y,input_list))

#*******?????????????******Descending Order**********???????????????????***#
no=[22,32,88,2,95]
no2=[58,92,32,4]
def _merge_and_sort_sample_(a, b):
    a.extend(b)
    # Create a new list
    new_list = []
    # Loop until a becomes empty
    while a:
        # set an arbitrary element as the minimum
        # in this case we chose the first index
        maximum = a[0]
        # loop through the list and
        # find the element that is smallest
        for element in a:
            if element > maximum:
                maximum = element
        # append the smallest element to the new list
        new_list.append(maximum)
        # now remove that smallest element from the original list
        a.remove(maximum)
    # Ultimately a will become empty
    # and the loop will end
    # now return the new list
    return new_list
print(_merge_and_sort_sample_(no,no2))
#*????????????????******Asscending Order******????????????????????****#
no=[22,32,88,2,95]
def _custom_bubble_sort_sample_(original_list):
    # This is an implementation of the
    # famous bubble sort algorithm
    # This can a very inefficient algorithm
    # when used with large data
         
    # our purpose here however is to show how to sort
    # a list without any built-in methods
	

    # make a copy of the original list
    my_list = original_list[:]
  
    # get the length of the list
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            # if next element is greater element then swap them
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list
print(_custom_bubble_sort_sample_(no))
 


