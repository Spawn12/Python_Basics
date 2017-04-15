#*******************************While Loop*************************************#
#As long as condition is true while loops run

no_of_cookies=int(input("How many cokies u want to eat : "))
ate_cookies=0
while no_of_cookies>0 : #given condition
    no_of_cookies=no_of_cookies-1 #it menas that every time te loop run it subtract 1 from remaining cookies until while condition became false
    ate_cookies=ate_cookies+1
    print("I have ate ",ate_cookies," cookies and ",no_of_cookies," cookies left")
print("I ate all")


#*******************Square root***************#

no=float(input("Enter a no for accurate Square root : "))
guess=no/2
accuracy=0.01
itteration=0
while abs((guess**2)-no)>accuracy :
    guess=(guess+(no/guess))/2
    itteration=itteration+1
    print("no of guesses",itteration,"guess ",guess)
print("Orignal number ",no)
print("Square root of the no ",guess)

#***************Sum of given no which is diviseble by give no************#
user_input=int(input("Enter Valid no"))
user_input1=int(input("Enter Valid no which have to divide by the no : "))
if user_input<=0 and user_input1>0 and user_input1<=user_input :
    print("Invalid no...") 
else:
    no=0
    x=0
    while no<user_input :
        no=no+1
        if no%user_input1==0:
            x=x+no #we initlize x=0 then evry time the loop run it will add the divisible no in x and beceme new value of x
            print (no)
print ("The sum of all divisible no is ",x)

#***************************Factorial**************************************#

user_input=int(input("Enter any no.. : "))
if user_input<=0: 
    print("Enter valid no...")
else :
    x=1
    no=1
    while no<=user_input:#As long as condition is true while loops run
        x=x*no
        no=no+1
print(x)

#************************sum of every third no****************************#
user_input=int(input("Enter no for sum of every third no starting from 1 : "))
x=-2
y=0
while x<=user_input:
    x=x+3
    y=y+x
    print(x)
print("sum of every third no ",y)


#***********************************For Loop***********************************************#
#When u want to repeat piece of code for a given no of time

my_books=["cat",2.5,2,True]
for x in my_books: #ever time the valu of x change by the element in list
    print(x) #x is the element in lists
print("No more Books")


my_no=[1,2,3,4,5,6] #This approach is not good of creating list insted we use function range
for x in my_no:
    print(x)
    print("Hello") #it will print hello 6 times


for current_no in range(1,11) : #range is an function we give till the desire no of loop+1
    print("Iteratation",current_no," Hey")

#*********************program which prints the sum of all the even numbers from 1 to 101.*********************#
user_input=int(input("Enter no to find even no : "))
y=0
for x in range(1,(user_input+1)):
    if x%2==0:
    #if x%2!=0: #for odd no
        print(x)
        y=y+x
print("Sum of given even no : ",y)

#*****************************Sum of all given no***********************#
n=int(input("Enter an no.. : "))
y=0
for x in range(1,(n+1)):
    print(x)
    y=y+x
print(y)

#****************sum of square of given no************************#
n=int(input("Enter no for sum of square of given no"))
y=0
#z=0
for x in range(1,(n+1)):
    #z=x**2
    #print(z)
    #y=y+z
    y=y+(x**2)
print("Sum of all square no ",y)


n=int(input("Enter an no for power of 10 : "))
y=0
for x in range (0,(n+1)):
    y=(10**x)
    print(y)

#***********************Continue and Break*******************************#

count = 20
for x in range(0,10):
    count = count - 1
    if x == 2:
        break
    print(count)
print(count)

k = 1
while k<5:
    if k % 7 == 0:
        break
    k = k + 2
    print(k)

my_list = ["dog", 24, "cat", 12]
count = 0
for element in my_list:
    if element == "cat":
        continue
    count = count + 1
    print(count)

for x in "computer":
    print (x))

for x in "computer":
    if x==p:
        continue #wheen the x goes on to p it will ignore and move forward
    print (x)

for x in "computer":
    if x==p:
        break #when the x goes on to p it will break all for loop and move come out of the loop
    print (x)

my_list = [6, 5, 7, 2, 3, 5, 7, 8] 
count = 0
for number in my_list:
    if number == 5 or number == 7: #whenever it come on 5 or 7 it will ignore that no
        continue
    else:
        count = count + number
print(count)




