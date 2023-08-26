#!/usr/bin/env python
# coding: utf-8

# # nested loop

# In[1]:


for i in range(0,4):
    print("Hello")
        
    for j in range(10,13):
            print(j,"user")


# In[2]:


for outerValue in range(1,4):   #pattern , row means outer loop and column means inner loop
    
    for innerValue in range(1,outerValue+1):
        print("*",end=" ")                                #end = " " value will be printed with a space
        
    print("")                                              #for getting it to a new line 


# In[3]:


print("*", end=" ")
print("hello")


# In[4]:


for outerValue in range(1,5):   #pattern , row means outer loop and column means inner loop
    
    for innerValue in range(4,outerValue-1,-1):
        print("*",end=" ")                                #end = " " value will be printed with a space
        
    print("")                                             #for getting it to a new line 


# In[5]:


##write a program to identify the input given by the user satisfy the following condition

   ## input should have a capital letter from A- Z
   ## input should have a small letter from r to z
   ## input should have a number 
   ##and should have a minimum of 6-15 character
    ##and it should have any character from @,#,$
    ##if all the condition is satisfy them print password is correct otherwise password is incorrect 
    
    


# # list : datatype
# # collect multiple data element
# # and data can be of different type 
# #index position and it is mutable 

# In[6]:


mylist=[19,30,56,33,85]
print(type(mylist),mylist)


# In[7]:


mylist=[19,30,56,33,85]
print(mylist[0:4:2])


# In[8]:


mylist=[19,30,56,33,85]
mylist[0]=22   #data on any position can be changed
print(mylist[0:4:2])


# In[9]:


mylist=[19,30,56,33,85]
mylist.append(1000)      #append will add the single value at a time.
print(mylist)


# In[10]:


mylist=[19,30,56,33,85]
mylist.extend("hi")            
print(mylist)


# In[11]:


mylist=[19,30,56,33,85]
mylist.extend(["hi",1000])     #value is passed through a list[]            
print(mylist)


# In[12]:


## to remove from the list using pop method


mylist=[19,30,56,33,85]
mylist.pop()              #pop will remove the elements from the list 
print(mylist)


# In[13]:



mylist=[19,30,56,33,85]
mylist.pop(0)              #pop will remove the elements from the index as well
print(mylist)


# In[14]:


# remove() will remove the value given in the bracket


mylist=[19,30,56,33,85]
mylist.remove(30)              #remove will remove the data written in the bracket  
print(mylist)


# In[15]:


#del will delete the memory reference 

mylist=[19,30,56,33,85]
del mylist[0]             #del will delete the memory reference  
print(mylist)


# In[16]:


# copy()
# insert()
# drop()


# In[17]:


# help(mylist)    #will give all the details about the the function


# In[18]:


# make a list check that it is interger type then create a square and append in the new list 


mylist=[2,3,4,4,"djdjd"]
li=[]

for i in mylist:
    if(type(i)==int):
        li.append(i**2)

print(li)
    
    


# In[19]:


#take a input string from the user and find out the first occurence of all the words


# In[20]:


#palindrom => SARAS, NAMAN

data="SARAS1"
if(data==data[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")


# # tuple: immutable (this is the only difference from list and also it has smaller size hence fatser than list )
# 
# 

# In[21]:


mytuple=10
print(type(mytuple))


# In[22]:


mytuple=10,"hey"     # tuple can have mixed types of values 
print(type(mytuple))    #paranthesis is optional but it should be seperated by comma


# In[23]:


mytuple


# In[24]:


mytuple[1]


# In[26]:


print(mytuple)
print(id(mytuple))
mytuple=mytuple + (60,50)
print("new",mytuple) 
print(id(mytuple))


# In[ ]:


# #take input from the user and do the following task 
# if input=1
# print the current data of os system
# if input=2
# create a folder with name regex folder on desktop
# if input=3
# copy the current file in the regex folder on desktop
# if input=4 
# open a browser and search for regex software on google
# if input=5- user => 5
#     Drop a whatsapp msg to Nidhi mam
  


# In[27]:



1
12
123
1234




for outerValue in range(1,5):   
    
    for innerValue in range(1,outerValue+1):
        print(innerValue,end=" ")                               
        
    print("")   


# In[28]:


# # A
# # AB
# # ABC


for outerValue in range(65,70):   
    
    for innerValue in range(65,outerValue+1):
        print(chr(innerValue),end="")                               
    print()   


# In[29]:



value=0
for outerValue in range(1,4):
 for innerValue in range(outerValue):
     value=value+1
     print(value,end="")
 outerValue=outerValue+1
 print("")


# In[30]:



    
outvalues = 4 
for i in range(outerValue):    
    print(" " * i, end="")
    
    print("*" * (outerValue- i))


# In[31]:


char=65 
for outerValue in range(65,70):   
    
    for innerValue in range(65,outerValue+1):
        print(chr(innerValue),end="")                               
    print()   


# In[32]:


outerValue = 4  
char= ord('A')  #ord retruns a Unicode of a given character
for i in range(outerValue):
    for j in range(i + 1):
        print(chr(char), end="")
        char += 1
    print()  # Move to the next line after each row
    


# In[33]:


import re

def pass_check(password):
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[r-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
  
    if not 6 <= len(password) <= 15:
        return False
  
    if not re.search(r'[@#$]', password):
        return False
    
    return True

user_input = input("Enter a password: ")

if pass_check(user_input):
    print("Password is correct.")
else:
    print("Password is incorrect.")


# In[35]:


def find_unique_words(input_string):
    words = input_string.split()  # Split the input string into a list of words
    unique_words = set(words)      # Convert the list to a set to get unique words
    return unique_words

user_input = input("Enter a string: ")
unique_words = find_unique_words(user_input)

print("Unique words:", " ".join(unique_words))


# In[ ]:





# In[ ]:




