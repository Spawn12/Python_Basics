#************************** Strings ********************************#
#String is an Sequence of Character and closed in single and double qutation
#String are immutable means once it has been created u cant chage or delete it but can append it
a="Earth"
print("He sai Hi to \"Taha\" ")
print(len(a))
print(a[2])
print(a[-2])
b="Mars"
print(len(b))
c=a+b # concanate value of a in to b
print(c)
print(len(c))
d=a*3 # it will print string value of a 3 times
print(d)
x='25' #it is an String with 2 character which is 2 and 5
y=25 #it is an integer
#print(x+y) # it can no add both because they are with different data type
z=int(x)+y # we convert value of x into an intger and similarly we can do with string 
print (z)

x = "abcdefg"
print (x[-6:len(x):2]) 

x = "abcdefg"
print (x[-4:-1:2])

a=" hello My name IS taha and im new to these languages \t\nPython\nMachine Learning \tData Science " # it's an string line
b=26
print(a.title()) #title is an method for The String in tittle way
print(a.upper()) #upper is an method for upper case
print (a.lower()) #lower is an method for lower case
print(a.rstrip())#we can remove extra space from right side is rstrip
print(a.lstrip())#we can remove extra space from left side is lstrip
print("Happy ",b,"rd Birthday")


#*****************************
def func(n):
    x=0
    while x<n:
        x=x+1
        x=str(x)
        print(x*int(x))
        x=int(x)
a=int(input("Enter any number : "))
func(a)
#***************************
def func(n,character):
    x=0
    while x<n:
        x=x+1
        a=character*int(n)
        print(a)
n=int(input("Enter an no to print character at that time : "))
char=(input("Enter ur character to print : "))
func(n,char)
#***************************
#n=8
start=n
x=0
def func (n):
    while x<n:
        n=n-1
        print(n*"*")
func(8)

def func (n):
    x=0
    list=[]
    while x<n:
        x=x+1
        list.append(x*"*")
        for y in list:
            abc=0*0 #null value
        print(y)
func(10)

#******************************* Character Encoding **************************#
#Each character is given a unique number(code) so it can be stored in a computer memory

print(ord('a')) #ord it's an built-in func for alphabetic returning its code
print(ord('S'))
print(chr(97)) #chr it the reverse of ord means which cahracter represent 97
print(chr(83))

values=""
for x in range(50,90):
    values=values+chr(x)
print(values)

def func(n):
    list=[]
    for x in range(n):
        list.append(chr(x))
    return list
print(func(100))
#****************** Return ASCII chracter ******************************#
def func(n):
    value=chr(n)
    return value
print(func(83))

#******************* Return number which is associated with ASCII character *********************#
def func(x):
    return ord(x)
print(func("*"))

#********************* Return the sum of value of cahracter in string***********************#
def func(strng):    
    list=[]
    for x in strng:
        if x.isalpha():
            list.append(ord(x))
            print ("the value of character",x," is : ",ord(x))
    return sum(list)
print ("Sum of all the value in cahracters : ",func("h ell*875o 56 /*t265264343##$A24**h320.a"))

#******************************* String Method ********************************#
x="He who would learn to fly one day but first learn to stand and ealk and run "
print(x.count("and")) #count the cahracter and
print(x.count("w")) #count the cahracter w
print(x.count("w",5)) #count the cahracter w with specifying the starting point
print(x.count('w',5,9)) ##count the cahracter w with specifying the starting and end point
print(x.replace("and","ZZZ")) #it will replace the and with ZZZ and give it to u but not change orignal string
y=x.replace("and","ZZZ")
print(y) #it will replace the and with ZZZ and assign to y with new replace string
z=x.replace('and',"mmM",2) #it will replace the and with ZZZ only 2 times from start and give it to u
print(z)
my_list=x.split() # it will spilit every word from "space" and append in my_list
print(my_list,"\n",x)
my_list=x.split("n") # it will spilit every word from give character in this case "n" and append in my_list
print(my_list,"\n",x)

#***************************************************************************#
my_str = "Hello"
print (my_str.islower())

my_str = "Goodbye"
print (my_str.lower())

my_str = "GoodBye"
print (my_str.isupper())

my_str = "Hello"
print (my_str.upper())

my_str = "GoodBye"
print (my_str.swapcase())

my_str = "computer science engineering"
print (my_str.title())

print ("hello".isalpha())

my_str = "hello there"
print (my_str.isalpha())

my_str = "hello12"
print (my_str.isalpha())

my_str = "CSE1309"
print (my_str.isalnum())

my_str = "CSE-1309"
print (my_str.isalnum())

print ("bird".endswith("ir"))

my_str = "PYTHON"
print (my_str.ljust(10,'x')) # it will join x to the string till 10 index

my_str = "abcdecebacd"
print (my_str.rfind("c", 3, 10))

x = "bye bobob"
print (x.strip("b")) 

x = ["dog", "cat", "pet"]
print ("ZZ".join(x)) #it will joix ZZ with every element of x

x = "Cat Dog"
print (x.swapcase()) #it will swap the case

a  = "CSE"
print (x.center(9,"x")) # it will put given string in center of x till given index which is 9 in this case

