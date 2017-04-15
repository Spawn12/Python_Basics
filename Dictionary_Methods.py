#********************** Dictionary Methods *************************#
data={"name":"Mark","age":28,'weight':78,"height":6.1,"native":"Polish","citizen":"Candian","profession":"Electrical Enginers","language":["English","Polish","Denish"],"father name":"Auston","martial status":"Divorsed"}
for x in data:
    print (x)
for x in data:
    print (data[x])
for x in data.keys():
    print (x)
for x in data.values():
    print (x)
for key,value in data.items():
    print("\n",key)
    print(value)
#data.clear() # it will clear the dictionary
#print(data)
    
#get method 
a=data.get("weight") # it will get the value of weight in dictionary data
print(a)

c=data.get("Job") # it will get the value of job if it does not find it will give None
print(c)

c=data.get("Job",25) # it will get the value of job if it does not find it will give 25
print(c)

#b=data["Job"] # it is same as get method but it will give error when the key is not present in a dictionary 
#print(b)

#data.pop
x=data.pop("native") # it will give the value to u and remove the element from dictionary
print(x)

#data.update(pet)
pet={'pet_type':'Cat','pet_color':'White','pet_breed':'Persian','pet_name':'Stephne'} # if we gave the same key as in data it will updated bte new value of that key
data.update(pet) #it will append the items of pet in data dictionary and pet dictionary itself not changed
print (data,"\n",pet)

#********************** Sorting Keys of Dictionary *****************#
def func(dict):
    x=list(dict.keys())
    x.sort()
    return x
print(func(data)) #return only sorted list of keys

#********************** Sorting Values of Dictionary *****************#
def func(dict):
    x=list(dict.values())
    x.sort()
    return x
#print(func(data)) #return only sorted list of values

#**********************
student={"Allen":[65,95,78],"Mark":[78,79,82],"Jack":[98,95,77],"Joseph":[79,82,89]}
def func(dict):
    z=True
    for x in student.values():
        for y in x:
            if y>=78:
                #print(y)
                z=True
    if z:
        print (student.keys())

func(student)
