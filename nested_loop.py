#*****************************Nested Loop*************************************#
#***************Finding Prime No*************************************#
no=23
#divisor=2
number=True
for divisor in range(2,no):
#while divisor<no:
    if no%divisor==0:
        number=False
        break
   # divisor=divisor+1
if number:
    print(no, " Prime no")
else:
    print(no," is not Prime no")


no=int(input("Enter start no : "))
end_no=int(input("Enter end no : "))
if no<=0 and end_no<=0:
    print("Your no is invalid...")
else:
    y=0
    for no in range(no,(end_no+1)):# no<=end_no:
        divisor=2
        number=True
        #no=no+1 #we dont use this statemenet with for loop 
        while divisor<no:
            if no%divisor==0:
                number=False
                break
            divisor=divisor+1 
        if number:
            print(no, " Prime no")
            y=y+no
    print("Sum of all prime no....: ",y)

