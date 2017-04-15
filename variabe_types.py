a=20.85
b=5+a
B=b*2
c=a+b
d='hello'
e=False
f=8/2
print ("this is a",a,"this is b",b,"this is B",B,"this is c",c,type(a),type(d),type(e),type(f))
#**************************Taking Input From User******************************#
x=input("What is ur name : ") #prompt is optional
print ("Glad to meet u ",x)
y=input() #the input func return string even we give int
print ("the user input is ",y)
z = int(input("how many children do you have?"))
print (type(z))#type of variable
#**************************This Program is to Convert from Celsius to Fahrenheit*************#
user_input=input("Plese input a temprature in Celsius:")
#user_input=float(input("Plese input a temprature in Celsius:")) #we can also changge the type here
celsius=float(user_input)     #converting string user_input into float celsius
fahrenhiet=((celsius*9)/5)+32
print(fahrenhiet)
#***********************************List(Data Type)*****************************#
my_list=["hello",324,5.2,False] #in + indexing no goes left to right and  for - indexing it start from -1 to right to left
print(my_list[1]+my_list[-2]) #tonford,anesthesia
print(my_list)
print(my_list[1])  #accesing third element in my list

x = [5, 'dog']
y = ['cat', 3.5]
print(x + y)

x = [ 5, 'dog']
print(3 * x)
#*************************Quiz1*******************************************#
x=int(input("Enter an number : "))
y=((x*x)-(12*x))+11
print (y)

sample_list = [2, 10, 3, 5]
x=(sample_list[0]+sample_list[1]+sample_list[2]+sample_list[3])/4
print(x)


x=int(input("Enter no for any Day : "))
y=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
z=x-1
print(y[z])

sample_list = [2, 10, 3, 5]
x=(sample_list[0]+sample_list[1]+sample_list[2]+sample_list[3])
print (x/4)

x=int(input("Enter Yur Age : "))
y=x*365
print("You are days ",y," old")
  
