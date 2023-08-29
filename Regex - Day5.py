#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dictionary

#key-value pair => mutable , and it stored the data  in the fomr of #key -value pair 

#key --- Identifier = value(data for the key)
#key - uunique 
#value - data (unique or it may duplicate )


# In[ ]:


#mutable datadypes , ordered but without any index positions.


# In[17]:


#key :value 
#key are unique => immutable data type

mydict = {1:"tushar" , 2:"yash", "greetings":1000}


# In[7]:


mydict


# In[8]:


mydict["greetings"]


# In[9]:


mydict["greetings"]=5000


# In[10]:


mydict["greetings"]


# In[11]:


mydict["300"]="aman"


# In[12]:


mydict


# In[20]:


mydict.pop("greetings")  #pop() method deletes the data and it retuns the value hence we can store it in a variable


# In[21]:


mydict


# In[22]:


mydict.popitem() #popitem deletes the last item from the list and returns the key and value


# In[23]:


mydict


# In[24]:


mytuple=(10,20)


# In[25]:


a,b= mytuple   #tuple unpacking, it distributes the data in 2 variables 

print(a)
print(b)


# In[ ]:


list1 = [(10,20),30] #list has 2 elements. 1 is tuple and second is 30


# In[28]:


list1=[(10,20),(30,40)]
for i in list1:
    print(i)


# In[30]:


list1=[(10,20),(30,40)]
for i in list1:
    a,b=i
    print(a)


# In[31]:


list1=[(10,20),(30,40)]
for a,b in list1:
      print(a)


# In[34]:


mydict = {1:"tushar" , 2:"yash", "greetings":1000}    #unpacking can be done in dictionary as well 


for i in mydict:
    print(i,mydict[i])


# In[37]:


mydict = {1:"tushar" , 2:"yash", "greetings":1000}   

for i in mydict.values():
    print(i)


# In[38]:


mydict = {1:"tushar" , 2:"yash", "greetings":1000}   
mydict.items()        #dictionary contains a list


# In[39]:


for i in mydict.items():
    print(i,type(i))


# In[40]:


mydict = {1:"tushar" , 2:"yash", "greetings":1000}   
for key,value in mydict.items():
    print(key,value)


# In[51]:


#del is remove items.In dictionary if the key is deleted value will automatically be deleted.


# In[52]:


mydict = {1:"tushar" , 2:"yash", "greetings":1000}   
del mydict[1]


# In[53]:


mydict


# In[56]:


# #question - take a list, occurence of every element and print it in a dictionary format

# list = [10,20,30,44,30,40]
# for i in list:
#     print 


# In[78]:


#Set => a collection of elements 
#set is mutable , set are unordered collection 
# no index position , elements are unique
#hetergenous 
#set is mutable but stores the elements which are immutable 
# it will give a collection of unique elements and unordered.

myset ={10,20,30,40,40,50,"hey",}     
print(myset)


# In[61]:


myset.add(100)  #add will add single element


# In[79]:


myset


# In[80]:


#update()will updated the multiple values
#iterable - on which we can run a loop 

myset.update("hey") 
myset


# In[81]:



myset.update(["omg",99,88]) 
myset


# In[73]:


#remove method will remove but while running it again it will give an error. Use #discard instead, it will skip while running again 
myset.remove(10) 
myset


# In[74]:



myset.discard(20) 
myset


# In[77]:


myset1={10,20,30}
myset2={20,30,30,50}

myset2.intersection(myset1)


# In[84]:


#issuperset
#disjoint
#symmetric difference update
#difference


myset1={10,20,30,50}
myset2={20,30,30,50}

myset1.issuperset(myset2)


# In[98]:


myset1={10,30,50,40,80}
myset2={20,50,60}

myset1.isdisjoint(myset2)


# In[96]:


myset1={10,20,30,50,40,80}
myset2={20,30,30,50,60,80}
result=myset1.symmetric_difference_update(myset2)

print('myset1 ', myset1)
print('myset2 = ', myset2)
print('result = ', result)


# In[94]:


myset1={10,20,30,50,40,80}
myset2={20,30,30,50}

myset1.difference(myset2)


# In[ ]:


# #function => functions are block of code which can be used multiple times
# #template  => with a statement can be used again and again


*********
# def functionname():
#     statement 
*********


# In[99]:


#function declaration 

def greeting():
    print("hey user")


# In[101]:


# function calling

greeting()
greeting()
greeting()


# In[106]:


#username is a variable which is a parameter

def greeting(username):
    print("hey user",username)


# In[108]:


#function call => arguement 


greeting("tushar")
greeting("aman")


# In[121]:


def add(a,b):
    print(a+b)
    
def multiply(a,b):
    print(a*b)


# In[115]:


add(10,20)


# In[116]:


multiply(10,20)


# In[124]:


def companyDetail(eid,fname,email):
    print(f"Eid is : {eid} \nFirst Name :{fname} \nEmail :{email}")
    
companyDetail(1,"tushar","tushar@gmail.com")


# In[126]:


companyDetail(2,"akansha","akansha1901@gmail.com")


# In[133]:


def func(x):
    print("x :",x,id(x))


# In[134]:


age=10
print("Age",id(age))

func(age)


# In[139]:


def listadd(mylist):
    print(mylist)
    
list1=[9,11]
listadd(list1)


# In[141]:


def listadd(mylist):
    print(mylist,id(mylist))
    mylist[0]=100
    
list1=[9,11]
listadd(list1)

print(list1,id(list1))


# In[143]:


# Types of Arguements
# life scope of variables
# Revision of all the classes


# In[ ]:




