#***************************Conditional*****************************#
x=int(input("Plese input a temprature in Celsius:")) 
fahrenhiet=((x*9)/5)+32
if fahrenhiet>90 :
    print("it's hot")#we have to give tab after the if and else condintion because it means its in the loop
elif fahrenhiet<30 :
    print("Its not cold")
else :
    print ("its owsome")
print(fahrenhiet)

x = 5
if 5 in [1, 2, 3, 4]:
    x = x + 1
elif 4 == 2:
    x = x + 2
elif 7 > 4: #this statement is true
    x = x + 3 #the value of x we initilize is 
else:
    x = x + 4
print (x)

x = 5
if 8 % 4:
    x = x - 1
elif 3 < 4 / 2:
    x = x - 2
elif "t": #this statetement is true
    x = x - 3
else:
    x = x - 4
print (x)

x = 12
if "x" in "meow" and 4 > 2+1 :
    x = x / 2
elif 6 % 2 != 0 :
    x = x / 3
elif 2 in ["cat" , "dog" ]:
    x = x / 4
else:
    x = x + 1
print (x)

x = 100
if x > 10 : #this statement is true then it move to next if 
    x = x + 10 #110     
if x > 20 : #this statement is also true 
    x = x + 50 #160
else:
    x = x + 70
print(x)


#********************************************************************#
if 0:
    print('yes')
else:
    print('no')

if 6 != 8 and 3 > 1:
    print('both')
else:
    print('none')

if "a" in "there" or 6 % 2:
    print('true')
else:
    print('false')

my_list = [ "cat", 2, "dog", 4]
x = 5 in my_list
if x:
    print('yes')
else:
    print('no')

my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'w' in my_list:
    print('true')
else:
    print('false')

my_list=[ 2.3, 'car', 12, 46, 'cat']
if 12 in my_list:
    print('hello')
elif 6 > 4:
    print('bye')
else:
    print('nothing')
x=str(input("Enter any string : "))
if 'dog' in x:
    print('Yes')
else:
    print('No')

my_list=[ 2.3, 'car', 12, 46, 'cat']
if 12 in my_list:
    print('hello') #if first statement is true it never move to other condition
elif 6 > 4:
    print('bye')
else:
    print('nothing')

my_string="hello"
if 10 % 5:
    print('true')
elif "le" not in my_string :
    print('false')
else:
    print('none')

if 6 <5:
    print('one')
elif 7 == 9 :
    print('two')
print("three")
#**********************************QUIZ******************************************#
x=str(input("Enter any string : "))
if "dog" in x and "Cat" in x :
    print("Dog")
elif "cat" in x :
     print("Cat")
elif "dog" in x :
    print("Dog")
else :
    print("None")

x=int(input("Enter ur age : "))
if x<=0 :
    print ("UNBORN")
elif x>0 and x<150 :
    print ("ALIVE")
elif x>150 :
    print ("VAMPIRE")

n=int(input("Enter possitive no : "))
if n<0 :
    print("Enter + no...")
elif n%3==0 and n%2==0 :
    print("BOTH")
elif n%3==0 or n%2==0 :
    print("ONE")
elif n%3==0 or n%2!=0 :
    print("NEITHER")

seconds=int(input("Enter Seconds : "))
if seconds<0 :
    print("Plzz Enter valid seconds")
else :
    x=seconds%(24*60*60)
    y=x%(60*60)
    z=y%60
    days=(seconds//(24*60*60))
    hours=(x//(60*60))
    minutes=(y//60)
    seconds=z
    print(days," days",hours," hours ",minutes," minutes ",seconds," seconds ")


# Type your code here
#n=int(input("Enter total no of Hours u work in a Week : "))
#if n < 0 or n > 168 :
  #  print("Invalid Hours...")
 ##if n>0 and n<=40 :
     #hourly_rate1=8
     #x=n*hourly_rate1
 #if n in [41,42,43,44,45,46,47,48,49,50]
    # hourly_rate2=9
     #y=(n-40)*hourly_rate2
    # z=x+y
# if n>50 :
     #hourly_rate3=10
     #a=
     #b=


n=int(input("Enter Ur weekly hours : "))
if n<0 and n>168 :
    print("Enter Valid Weekly Hours...")
if n>0 and n<=40 :
    n=n*8
if n>40 and n<=50 :
    x=n-40
    n=x*9
else :
    print (n)

#********************************************#
requested_topping=[]
if requested_topping:
    for value in requested_topping: #this loop will be run if the upper condition is  true
        print("Adding ",value,".")
    print("\nFinished making your pizza!")
else:
    print("Are u sure u want to eat plane pizza......")

