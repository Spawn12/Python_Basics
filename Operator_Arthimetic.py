#**********************************Arthimetic Operators********************************#
x=9//2 #floor division
print (x)
x=9/2 #simple division
print (x)
x=9%2 #modolus
print (x)
x=2**3 #power
print (x)
x=2*(3+4)
print (x)
print (40*4/20*5)
print (int(8.5/4))
print (int(8.5)/4)

#*****************************Relational Operator****************************#
#Relational Operators have lower Precedents than Arthematic Operators
print(5>4) #asking python is 5 greater than 4
print (5==4) #testing the equality of two operands
x=4 #initializing the value to x
print(x==3)#asking python is x is equal to 3 which we give the value 4
print(x!=3)#not equal
print (5>=5)#equals to or greater than

#******************************Logical Operator******************************#
#Logical Operators have lower Precedents than All Operators
x=(5>2) and (3>6) #and opertor is True if both are true
print(x)

x=(5>2) or (3>6) #or opertor is True if one are true
print(x)

x=not (8>6) #not opertor is True if the statement is true and it Unirary Operator in this case statement is False
print(x)

#*****************************************************************************#
print( not 0)

a = 8 > 6
b = 0 < 5
print( a and b)

a = 8 == 8.1
b = 2 >= 5
print( a or b)

print(not not (5 > 4))

#**************************Membership OPerator*****************************#
#Membership operator are only two type in and not in and have higher Presedence than Logiacl Operator 
x=[6,"taha",5.8,True]
print(5.8 in x) #asking is 5.8 is present in the list of x which is True
print(5.9 in x) #asking is 5.9 is present in the list of x which is False
int('taha' not in x) #asking is taha is not present in the list of x which is False

x="HAMDARD UNIVERSITY"
print ('k' not in x)

x = [ 2.3, "dog", "disk", "donkey", 6]
print("d" in x)




