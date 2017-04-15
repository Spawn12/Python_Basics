#**********************************************************************#
#************** It will swap the character case ***********************#

def func(a):
    b=""
    for x in a:
        if x.islower():
            b=b+x.capitalize()
        else:
            b=b+x.casefold()
    return b
#print(len(a))
print(func("hElo i M neW"))

#***************** Return Character Without "Spaces" *********************#
def func(strng):
    b=""
    for x in strng:
        print (x)
        if x==(chr(32)): #chr(32) is ascii code for "space bar"
            continue
        else:
            #b=x+b #if we put x before b it will reverse the string
            b=b+x
    return b
print(func("Syed Taha Mashhadi"))

#**************** Reversing the String ***********************#
#Method 1
def func(input_str):
    result=""
    for x in input_str:
        print("value of x : ",x)
        print("value of result : "+result)
        result=x+result #if we put x before result it will reverse the string
        print("value of x+result : ",result)
    return(result)
a=" Hello are u there"
print(func(a))

#Method 2
def func(input_str):
    result=""
    for x in range(len(input_str)-1,-1,-1):
        print ("value at index ",x," is : ",input_str[x])
        result=result+(input_str[x])
    return result
print(func("hello are u there"))

#************************************************************#
print(a.split()) #Difference b/w two split method
list=[x for x in a]
print(list)
#******************* Calcuting the same given no of character in given string****************************#
def func(string,n):
    list=(string.split())
    result=0
    for x in list:
        if x.isalpha() and len(x)==n:
            result=result+1
    return result
a="He who would learn to fly but first he have to walk then run and in last he could fly in sky a"
print(list)
for y in range(1,11):
    print("There are total ",func(a,y)," word with ",y," character in given string : ")

#*********************** Palindrome(The word which is same as forward and backword i.e level,civic) *************************************#
def func(input_string):
    result_a=""
    result_b=""
    for value in input_string:
        result_a=result_a+value
        result_b=value+result_b
    if result_a.lower()==result_b.lower():
        return True
    else:
        return False
a="LeVel"
print("Ur given string ",a," is Palindrome : ",func(a))

#************************** Sorted lisdt *****************************#
list=['java', 'matlab','c','python']
def fun(list):
    my_list=[]
    for x in list:
        my_list.append(x)
    if list==sorted(my_list):
        return True
    else:
        return False
print("Is given list is sorted : ",func(list))

#***************** Counting no of vowels in list *******************#
def func (string):
    list=['A', 'E', 'I', 'O', 'U']
    count=0
    for x in string:
        for y in list:
            if x.upper()==y:
                count=count+1
    return count
a="ElEphAnT"
print("No of vowels in given string ",a," is : ",func(a))

#********************** Count the sum of given character in String ********************#
def func(string,character):
    count=0
    for x in string:
        if x.lower()==character.lower():
            count=count+1
    return count
a='supernovas are so awesome'
b='s'
print("The word is : ",a," : and the character is : ",b," : no of repetition of that character in that string is : ",func(a,b))

#********************* Count sum of starting from the given character ****************#
def func(string,character):
    count=0
    list=string.lower().split()
    character=character.lower()
    for x in list:
        if x[0]==character:
            print("The word starting form : ",x)
            count=count+1
    return count
print(func("an elephant's eye escapes earth", 'e'))

#********************* Count sum of word which have more than given length **********************************#
def func(string,n):
    count=0
    list=string.lower().split()
    for x in list:
        if len(x)>n:
            count=count+1
    return count
a="am i good or some food"
b=3
print("More than ",b," words in string : ",a," is :",func(a,b))

#****************????**********
def func(string):
    my_list=[]
    sum_list=[]
    list=[x for x in string.lower()]
    for x in list:
        if x.isalpha():
            my_list.append(x)
    print(my_list,"\nlength of my_list : ",len(my_list))
    for y in my_list:
        a=my_list.count(y)
        print(a)
        #if y==
        sum_list.append(a)
        #my_list.split(y)
    print(sum_list,"\n Sum om sum_list",sum(sum_list))     
#func("saf asfasf afGsafsdag hrewgegew fKDSDSaaf")

#************************ Reverse Swap of String **********************#
def func(string):
    count=""
    b=""
    for x in string:
        count=x+count
    for x in count:
        if x.islower():
            b=b+x.capitalize()
        else:
            b=b+x.lower()
    return b
a="hEllO pyThOn WorlD"
print("The reverse swap of : ",a," is :",func(a))

#**************************
def func(string):
    list=string.split()
    print(list)
    for x in range(0,len(list)):
        print(list[x])
        list[x]=list[x][::-1] #this reverse the single element of list
        print(list[x])
    count=""
    print(list)
    for y in range(0,len(list)):
        count=count+list[y] + " " #this statement will add element of list in count with " "
    count=count.strip() #it will strip out extra spaces
    return count
print(func("Hello are u there hey"))

#************************************* Assignment *************************************#
def find_mismatch(s1,s2):
    if len(s1)==len(s2) and s1.lower()==s2.lower():
        print(s1," and ",s2," are same")
    elif len(s1)==len(s2):
        print(s1," and ",s2," are same in length")
    else:
        print(s1," and ",s2," are not same")
(find_mismatch("sin","hiN"))

#*************************
def single_insert_or_delete(s1,s2):
    if len(s1)==len(s2) and s1.lower()==s2.lower():
        print(s1," and ",s2," are same")
    elif len(s1)+1==len(s2) or len(s1)==len(s2)+1 or len(s1)-1==len(s2) or len(s1)==len(s2)-1:
        print(s1," and ",s2," is same if we delete or add one character")
    else:
        print(s1," and ",s2," are not same")
(single_insert_or_delete("spoke","poke"))

#************************** Spell Check *****************************#
def func(s,correct_spelled):
    words=s.strip().split()
    output_str=""
    for current_word in words:
        if len(current_word)<=2 or (current_word in correct_spelled) :
            output_str=output_str+" "+current_word
            continue
        min_mismatch=2
        replacement_word=current_word
        for correct_word in correct_spelled:
            if min(_find_mismatch(current_word,correct_word), _single_insert_or_delete(current_word,correct_word))==1:
                replacement_word=correct_word
                break
        output_str=output_str+" "+replacement_word
    return output_str.strip().lower()
def _find_mismatch(s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 2
    return number_of_mismatches 
def _single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
s1="Thes is the Firs cas"
s2=['that','first','case','car']
print(func(s1,s2))

#**************** Count Consnant (all alphabets except vowels) ********************************#
def count_consonants(string):
    count=0
    vowels=["a","e","i","o","u"]
    for x in string:
        if x.lower() not in vowels and x!=chr(32):
            count=count+1
    return count
a="How are u tAha"
print("Total consnant in string : ",a," : is : ",count_consonants(a))

#**********************
def func(string):
    no_list=[]
    word_list=string.lower().split()
    answer=""
    for x in word_list:
        if len(x)>len(answer):
            answer=x
    return answer
a="hey How are u tAha what are u doing i m fine im currently studying "
print("The largest word in given string : ",a," : is : ",func(a))

#************************************* Anagrams *****************************#
#Two strings are anagrams if one string can be constructed by rearranging the characters in the other string using all the characters in the original string exactly once. 
def test_for_anagrams(string1, string2):
    if len(string1)==len(string2):
        for x in string1:
            if x in string2:
                True
        return True
    else:
        return False
a="Orchestra"
b="Carthorse"
print("Gven two string are : ",a,": and : ",b," : these are Anagrams : ",test_for_anagrams(a,b))
#****************************** Encrypted to secret character ***************************#
def func(string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key="Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted_message=""
    for x in string:
        index=character_set.find(x) #this statement will find the index of given character in string
        #print (index)
        encrypted_message=encrypted_message+secret_key[index] #this statement will give the chaater at given index 
    return encrypted_message

print(func("Lets meet at the usual place at 9 am"))
