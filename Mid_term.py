#******************************* Mid Term ***********************************#
x = ["dog", 2, "cat", 34, 5.8]
m = 0
print(len(x))
for i in range(len(x)):
    m = m + i
    print(m)
print(m)
print("#*********************************************#")

i = 1
while False:
    if i % 5 == 0:
        break
    i = i + 2
print(i)
print("#*********************************************#")

count = 0
list_1 = []
for i in range(1,4):
    list_1.append(i**2)
for x in list_1:
    count = count + x
print(count)
print("#*********************************************#")

my_list = []
for k in range(1,101,20):
    print(k)
    my_list.append(k)
print (my_list[: :2] )
print("#*********************************************#")
def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [1,5,3]
my_fun(m)
print(m)
print("#*********************************************#")
def my_fun(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values,-6,-4)
my_fun(values,2,4)
print(values)
print("#*********************************************#")
def my_fun(i):
    values = []
    values.append(i)
    return values
my_fun(5)
print(my_fun(3))
print("#****************** Most Divisor Number in Lisst***************************#")
#Method 1
def find_integer_with_most_divisors(input_list):
    divisor=0
    d_list=[]
    l_list=[]
    for x in input_list:
        #print(x)
        while x>divisor:
            divisor=divisor+1
            if x%divisor==0:
                d_list.append(divisor)

        if divisor>0 :
            divisor=0
        #print(d_list)
        a=(len(d_list))
        l_list.append(a)
        #print(l_list)
    
        if len(d_list)>0:
            d_list.clear()
    c=l_list.index(max(l_list))
    return (input_list[c])

#Method 2
def integer_with_most_divisors(sample_list):
    # first set max_divisors to 0
    max_divisors = 0
    max_divisors_item = None
    for items in sample_list:
        # create a list to hold the divisors of all items in the list
        output_list = []
        for number in range(1, items):  # Check for the remainder when k is divided by number
            if items % number == 0:                   # if the remainder is 0 that means number is a divisor of k
                output_list.append(number)  # append number to the output list

        length = len(output_list)# if the length of divisors for a particular element
        if length > max_divisors:    # is greater than the current one i.e max_divisors
            max_divisors = length
            max_divisors_item = items    # then set max_divisors as that length and max_divisor_item as
        return max_divisors_item      # that particular item
        
no=[8, 12, 18, 6,200,5,65]
print(find_integer_with_most_divisors(no))
print("#*********************************************#")
def func(n):
    new_list=[]
    y=0
    z=True
    for x in range(2,n):
        y=y+x
        if x%y==0:
            z=False
    if z:
        new_list.append(x)
    return new_list
#print(func(25))
print("#*************** Sum of Multiplying index of both list ******************************#")
a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]
def func (a,b):
    total=0
    new_list=[]
    list=0
    for x in range(0,len(a)):
        for y in range(0,len(b)):
            if x==y:
                total=(a[x]*b[y])+total
                list=a[x]*b[y]
                new_list.append(list)
    return total,new_list
print(func(a,b))
print("#************* Write a function called pattern_sum that receives two single digit positive integers, (k and m) as parameters and calculates and returns the total sum ********************************#")
def pattern_sum(a, b):
    total=0
    sum_of_list=0
    list=[]
    while b>len(list):
        total=(total*10)+a
        list.append(total)
    print (list)
    for x in list:
        sum_of_list=sum_of_list+x
    return sum_of_list
print(pattern_sum(5,3))
print("#******************  unique common elements ***************************#")
a=[5, 6, -7, 8, 8, 9, 9, 10]
b=[2,-7,-5,4,8,12,225,9,8]
def unique_common(a, b):
    list=[]
    #a.extend(b)
    for x in a:    
        for y in b:
            if x==y and y not in list:
                list.append(y)
    if len(list)==0:
        print("None")
    else:
        return list
print(unique_common(a,b))
print("#****************** List of all Prime no ***************************#")
#Method 1
def list_of_primes(n):
    list=[]
    list2=[]
    list3=[]
    z=True
    result=2
    for x in range(2,n):
       list.append(x)
       list2.append(x)
    for a in range(0,len(list2)):
         for b in range(0,len(list3)):
             if a%b==0:
                 print(a)
                 z=False
    if z:
        list3.append(a)
    return list3
print(list_of_primes(12))

#Method 2
def list_of_primes_sample(n):
    my_list = []
    integer = 2
    while integer < n:
        prime = True
        start = 2
        while start < integer:
            if integer % start == 0:
                prime = False
            start = start + 1
        if prime == True:
            my_list.append(integer)
        integer = integer + 1
    return my_list
print(list_of_primes_sample(13))
print("#*********************************************#")
n=int(input('please enter an integer between 1 and 9999: '))
one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_to_ninety=['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']
temp_str=""
if n==0:
    temp_str='zero'
    #print('zero')
first_digit=n//1000
second_digit=(n%1000)//100
third_digit=(n%100)//10
fourth_digit=(n%10)
if first_digit>0:
    temp_str=temp_str+one_to_ten[first_digit]+' thousand '
    #print (one_to_ten[first_digit],'thousand ',end='')
if second_digit>0:
    temp_str=temp_str+one_to_ten[second_digit]+' hundred '
    #print (one_to_ten[second_digit],'hundred ',end='')
if third_digit>1:
    temp_str=temp_str+twenty_to_ninety[third_digit]+" "
    #print (twenty_to_ninety[third_digit],'',end='')
if third_digit==1:
    temp_str=temp_str+ten_to_nineteen[fourth_digit]+" "
    #print (ten_to_nineteen[fourth_digit],'',end='')
else:
    if fourth_digit:
        temp_str=temp_str+one_to_ten[fourth_digit]+" "
        #print (one_to_ten[fourth_digit],'',end='')
if temp_str[-1]==" ":
    temp_str=temp_str[0:-1]
print (temp_str)

print("#*********************************************#")

