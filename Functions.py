#**************************Functions******************#
#Function is a piece of code which itself not run but can be use in main program and reduces the duplication of code

def a(name): #the given data type in argument is not specified so what u give it will return u
    print("Hello",name)
a(5) #calling a function

for k in range(1,6):
    print("k is equals to",k)
    a("Taha")
    
#**************************Square of a number*******************************#
def square_of_no(a):
    result=a**2
    return result
n=int(input("Enter an no for Square : "))
print (square_of_no(n)) #printing the func with passing user input argument in it

#********* function that accepts two positive integers  returns a list that contains the area and perimeter of that rectangle***********#
def a(height,width):
    area=height*width
    perimeter=2*(height+width)
    list=[area,perimeter]
    return list
print (a(1,3))

# ***********Function for sum of all the no in list****************************#
def k(a):
    y=0
    for x in a:
        y=y+x
        print (y)
    return y
a=[1,5,8,9,2,1]
print ("Sum of all elements in k is :",k(a))
#*****************Sum of all given no*******************************#
def k(a):
    y=0
    #x=0
    while y<a:
        y=y+1
        print (y)
    return y
#a=8
#print ("Sum of all elements in k is :",k(8))

#****************************Average of List**********************************#
def func_average(list):
    average=0
    y=0
    for x in list:
        y=y+x
    average=y/len(list)
    return average
list=[2,6.5,2,95]
print ("Average of list is : ",func_average(list))

#********************for max and min no*************************#
list=[2,5,8,1]
def largest_no(list):
    max_no=list[0]
    for x in list:
        #if x<max_no: #it is for min number
        if x>max_no:
            max_no=x
    return max_no
print (largest_no(list))

#********************* The magnitude of a vector is the square root of sum of squares of all the components of the vector.**************************#
import math
vector = [-1, 10, 3]
def mag_vector(vector):
    y=0
    a=0
    for x in vector:
        z=x**2
        y=y+z
    print(y)
    #answer=math.sqrt(y) #this is builtin math func for square root print square root of the answer
    answer=(y**(1/2)) #square root of y stored in answer
    g=answer**2
    print ("Sqare : ",g) #print squre of the answer
    return float(answer)

#???????for unit vector= individual value /magnitue??????????????????????#
    #for x in vector:
       # a=x/answer
        #list=[a,a,a]
    #return list
#????????????????????????????????????????????????????????????????????????#
print (mag_vector(vector))

#************************Area of an Circle***************************#
def area_of_circle(radius):
    pi=3.14
    area=pi*pow(radius,2) #pow is the builtin fun for the x to the  power y 
    return area
a=float(input("Enter Value of Radius : "))
print (area_of_circle(a))

#*********************************MODULE***************************************#
from math import *
#Module is the type of function file which we call in our main program
import module_my_math #importing file (approach 1)
#import module_my_math import * #(approach 2)(it will import all function we dont have to give file name)
number=int(input("Enter no : ")) 
x=module_my_math. odd_no(number)# #(approach 1)assigning value of x to ood_no function
# x=odd_no(number) #(approach 2)
print (x)

#***********************Evaluating expression***********************#
from math import *
def evaluate(x):
    y=(sin(x))-(cos(x))+((sin(x))*(cos(x)))
    return y
print (evaluate(22))


#***************************************Assignment***********************************#

def monthly_payment(principal, annual_interest_rate, duration):
    if annual_interest_rate==0:
        return principle/(duration*12)
    else:
        r=(annual_interest_rate/100)/12
        n=duration*12
        MonthlyPayment=principal*((r*((1+r)**n))/((1+r)**n)-1)
        return float(MonthlyPayment)

def remaining_loan_balance(principal, annual_interest_rate, duration , number_of_payments):
    r=(annual_interest_rate/100)/12
    n=duration*12
    p=number_of_payments
    if r==0:
        RemainingLoanBalance=principal*(1-(p/n))
        return float(RemainingLoanBalance)
    else:
        RemainingLoanBalance=principal*(((1+r)**n-(1+r)**p)/((1+r)**n-1))
        return float(RemainingLoanBalance)

principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
print("LOAN AMOUNT:",principal,"INTERST RATE (PERCENT)",annual_interest_rate,)
print("DURATION (YEARS): ",duration,"MonthlyPayment: ",(monthly_payment(principal, annual_interest_rate, duration)))
for x in range(1,duration+1):
    a=int(remaining_loan_balance(principal, annual_interest_rate, duration,x*12))
    b=int(monthly_payment(principal, annual_interest_rate, duration)*x*12)
    print("YEAR: ",x,"BALANCE: ",a,"PAYMENT: ",b)

#****Write a function that receives a positive integer as function parameter and returns True if the integer is a perfect number, False otherwise.
#A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to itself. For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and
#their sum is 1+2+3 = 6. Therefore, 6 is a perfect number.************# 
def func(no):
    y=0
    for x in range(1,no):
        if no%x==0:
            y=y+x
    if y==no:
        return True       
    else:
        return False
print(func(7))


#****************************************Prime Number*********************************#
def func(n):
    y=0
    z=True
    for x in range(2,n):
        y=y+x
        if n%y==0:
            z=False
    if z:
        return True
    else:
        return False
a=int(input("Enter no for prime number : "))
print("It is",func(a),"no")         

#???????????????????????????Finding LCM of two no?????????????????????????????????????????#
def _least_common_multiple_sample_(a, b):
    # first make a backup/copy of a
    copy_of_a = a
    # While the remainder when a is divided by b is not 0
    # continue to add a to its backup (copy_of_a)
    while (copy_of_a % b) != 0:
        copy_of_a = copy_of_a + a
    return copy_of_a
print ("LCM : ",_least_common_multiple_sample_(10,3))

#????Write a function that accepts two positive integers as parameters. The first integer is the number of heads and the second integer is the number of legs of all
#???the creatures in a farm which consists of chickens and dogs. Your function should calculate and return the number of chickens and number of dogs in the farm in a
#???list as specified below. If it is impossible to determine the correct number of chickens and dogs with the given information then your function should return None. Example 1, if your function received the following numbers:

def _sample_fun_puzzle_ (heads,legs):
    dogs=(legs-heads*2)/2
    if dogs<0 or dogs%1:
        return None
    dogs=int(dogs)
    chickens=heads-dogs
    if chickens< 0:
        return None
    return [chickens,dogs]
