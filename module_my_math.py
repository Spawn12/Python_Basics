import math
def area_of_circle(radius):
    pi=3.14
    area=pi*pow(radius,2)
    return area

def magnitute_of_vector(list):
    y=0
    for x in list:
        z=x**2 #for square of alement
        y=y+z #for sum of square of all element
    answer=y**(1/2)#for square root of sum of square of all element
    return answer
def sum_of_even_no_list(list):
    for x in list:
        y=0
        if x%2==0:
            y=y+x
    return y

def sum_of_odd_no_list(list):
    for x in list:
        y=0
        if x%2!=0:
            y=y+x
    return y
def even_no(no):
    if no%2==0:
        return no
    

def odd_no(no):
    if no%2!=0:
        return no
   
    
