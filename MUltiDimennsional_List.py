list=[["Taha",72,85],["Mark",69,72],["Joseph",84,91]]
print(list)
x=list[1][2] #assigning the 2 element of first list
print(x)
y=list[0] #assigning 0 element of list
print(y[0])
print(list[0][0][1]) #accessing 1st charcter in 0 elwment of in 0 list
#************** Finding Average of Student No in Test **********************#
list=[["Taha",72,85],["Mark",69,72],["Joseph",84,91]]
total_1=0
for x in list:
    total=0
    for y in range(1,len(x)):
        total=total+x[y]
    average=total/(len(x)-1)
    print("The average no of ",x[0]," is : ",average)

#***********************Sum and average of all no in 2D list***************************#
def func(no):
    total=0
    count=0
    i=0
    my_list=[]
    for x in no:
        for y in x:
            total=total+y
            if y%2==0:
                my_list.append(y)
            count=count+1
    for z in my_list:
        if i<z:
            i=z
    print("avrage of all no in list : ",total/count)
    print("greatest value in my_list : ",i)
    print("all values in given list are : ",my_list)
    return total
list=[[-18, 20, 13, 44], [-12, -6, 13, -44]]
print("total no in given list 2D ",list," is : ",func(list))

#************************ Maximmum even value in list ************************#
def func(no):
    i=0
    my_list=[]
    for x in no:
        for y in x:
            if y%2==0:
                my_list.append(y)
    for z in my_list:
        if i<z:
            i=z
    return i
list=[[121, -18, 20, 13, -44], [199, -12, -6, 13, -44]]
print("Maximum no of even no in 2D list is : ",func(list))
#********************* Sum of each row in List ***********************************#
def func(list):
    my_list=[]
    for x in list:
        my_list.append(sum(x))
    return my_list
a=[[1, 2, 3, 4], [2, 4, 6, 8]]
print("Sum of each list : ",func(a))

#*********************** Sum of each colunm in List ***************************#
def func(sample_list):
# Method 1:
# return [max(col) for col in zip(*sample_list)]
# Alternative Solution
    #cols = len(sample_list[0])
    mylist = []
    for x in range(len(sample_list[0])):
        column_sum = 0
        print (x)
        for y in sample_list:
            column_sum += y[x]
        mylist.append(column_sum)
    return mylist
list=[[1, 2, 3, 4], [2, 4, 6, 8]]
print ("Sum of colunm is : ",func(list))
