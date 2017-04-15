#*********************** Dictionaries **************************#
#A dictionary in Python is a collection of key-value pairs
Jack={"height":6.2,"colour":"white","weight":72,"age":28,"nationality":"Australia"} #it is the dictionary of Jack in which we stored his attributes by giving their key value
print(Jack['age']) #accessing the weight of Jack
print("nationality" in Jack) #asking the key in Dictionary Jack
#print(Jack[2]) #we cant access by the index
#Adding item to a Dictionary
Jack["profession"]="Banker" # new item added to Dictionary Jack 
for v in Jack:
    print (v) # accesing keys of Jack
    print (Jack[v]) #accessing keys value in Jack
for a in Jack.keys(): # it will extract all the keys it is helpfull for large amount of data
    print(a)

for a in Jack.values(): #it will extract all the values of keys from giving Dictinary
    print(a)

numbers={"one": 1, "two": [4, 6, 3], "three": 3}
x = (numbers["two"])
x.sort() #we can sort the list valiue in Dictionary
print(x)

#Accesing all the items in Jack with thier respective Keys
for key,value in Jack.items(): # pyhton dosen't care in Order 
    print("\nKey: ",key)
    print("Value:",value)

#We can add keys and thier values by...Dictionary name[key]=value
Jack["FatherName"]="Haton" # adding attributes of jack
Jack["native"]="English" # adding attributes of jack
print(Jack["FatherName"],Jack["native"],Jack["weight"])

#We can also change the value of a key byRedefining it
print(Jack["weight"])
Jack["weight"]=75 #redefing the value of weight
print("The new value of weight is : ",Jack["weight"])

#We can perform mathematical operations with the values like adding the value of height or weight
print(Jack["height"])
Jack["height"]=Jack["height"]+0.2
print(Jack["height"])

print ("Jack weight is : ",Jack["weight"],"Jack age is :",Jack["age"])
if Jack["age"]>12 and Jack["age"]<=20:
    Jack["weight"]=35
elif Jack["age"]>20 and Jack["age"]<=35:
    Jack["weight"]=75
elif Jack["age"]>35 and Jack["age"]<=60:
    Jack["weight"]=70
else:
    Jack["weight"]=72
print (Jack["weight"])

#deleting values with their keys
print(Jack)
del Jack["native"] # deleting values native with their "English"
print(Jack)

for value in Jack:
    if value=="weight": # finding weight of jack is 
        print ("The weight of Jack is : ",Jack[value])


#****************** Aliens ****************************#
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Alien x_position",alien_0['x_position'])
if alien_0['speed']=='slow':
    x=1
elif alien_0['speed']=='medium':
    x=2 
else:
    x=3 #This must be fast
alien_0['x_position']=alien_0['x_position']+x
print("Alien new x_position",alien_0['x_position'])

#******************* Poll For Favourite Language *****************#
favourite_lang={
    'taha': 'Python',
    'jack': 'PHP',
    'mark': 'Ruby on Rails',
    'phill': 'Java'
    }
list=['jack',"taha"]
for x in (favourite_lang):
    print("People who apply for BootCamp : ",x.upper()," for ",favourite_lang[x])
for y in list:
    if y in favourite_lang:
        print("Congrats u have choosen for BootCamp : ",y.upper()," for ur respective Language : ",favourite_lang[y])

#************************ Nesting of Dictionaries in List ***********************#
taha={"age":20,'weight':82}
mark={"age":23,'weight':86}
joseph={"age":10,'weight':35}
list=[taha,mark,joseph]
for x in list:
    print (x)
print("item of index 1 in list : ",list[1])

x=0
list=[]
for x in range(20): # for appending the the items of alien_x in list 20 times
    #x=x+1 #we cant assign the value of x in alien
    alien_x={'color': 'green', 'points': 5, 'speed': 'slow'}
    list.append(alien_x)
print(list[:5])
print(list.index(alien_x))# it will give 0 because all the elements in list have same name which is alien_x
print("Show how many element have been created in list : ",len(list))

#************************ Nesting List in a Dictionary *******************************#
pizza={
    'toppings':['chesse','chicken','veg'],
    'crust':'thick'
    }
print("You order the pizza with : ",pizza['crust']," -crust and with these toppings : ",pizza['toppings'] )

favourite_lang={
    'jen':['C++','XML'],
    'taha':['Python'],
    'mark':['Ruby','JQuery','HTML'],
    'hena':['Swift']
    }
print("it print items of Dictionary : ",favourite_lang.items(),"\nit only print values of Dictionary : ",favourite_lang.values(),"\nit only print keys of Dictionary",favourite_lang.keys())
for name,lang in favourite_lang.items():
    print("\n",name.title()," favourite languages are: ")
    print("\t",lang) # it will print whole list
    for x in lang: # loop for list
        print("\t",x.title()) #it will print elements of list

#************************ Dictionary nested in Dictionary **************************#
bio_data= {
    'taha':{"age":20,'weight':82,'last':'mashhadi'},
    'mark':{"age":23,'weight':86,'last':'kem'},
    'joseph':{"age":10,'weight':35,'last':'atwood'},
    }
for name,info in bio_data.items():
    print("Name : ",name.title())
    print("last name : ",(name+" "+info['last']).title())
    print("age : ",info['age'])
    print("weight : ",info['weight'])
