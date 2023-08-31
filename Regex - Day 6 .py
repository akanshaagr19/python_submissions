#!/usr/bin/env python
# coding: utf-8

# In[2]:


#python is a dynamic type langauage, we can avoid defining the data type at the time of function declaration 

def addNo(num):
    num=num+5
    print("Num value is:", num)

x=10
addNo(x)
print(x)


# In[ ]:


## To Leann 

#we need to swap the numbers without using third variable and with using a=b,b=a;


# In[6]:



#local 
def func(num):

    num=50
    print(num)

#global

num=10
print(num)
func(num)
print(num)


# In[7]:


#types of arguement passing

def company(eid,fname,email):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")


# In[8]:


#Type 1 

#required arguement 
company(2,"tushar","regex@gmail.com")


# In[9]:


def company(eid,fname,email):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")
        
#Type 2

#positional arguements
company("tushar",2,"regex@gmail.com")


# In[10]:


def company(eid,fname,email):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")
        
#Type 3

#keyword arguement
company(fname="tushar",eid=2,email="regex@gmail.com")


# In[11]:


def company(eid,fname,email):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")
        
#Type 3

#keyword + postional arguement but in this keyword arguement should be at the end. 


company(2,fname="tushar",email="regex@gmail.com")


# In[13]:


def company(eid,fname,email):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")
        
#Type 3

#keyword + postional arguement
company(2,"tushar",email="regex@gmail.com")


# In[14]:


def company(eid,fname,email):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")
        
#Type 3

#keyword + postional arguement
company(email="regex@gmail.com",2,fname="tushar",)


# In[15]:


#default arguement but it can be created in function declaration

def company(eid,fname,email="gmail.com"):
        print(f"Eid:{eid} \nFname:{fname} \nEmail:{email}")

company(20,"tushar","yahoo.com")


# In[23]:


##variable length arguement (args)and its like(or behaves) positional arguement but not exactly the same.
##keyword arguement will not work here 


def company(*data):
        print(data,type(data))
        
company(10,20,30,40,'hey',90)


# In[25]:


#keyword variable length arguement(kwargs) - sequence can be changed as per the condition 
#positional arguement will not work here

def company(**data):
        print(data,type(data))
        
company(hey=1,age=90)


# In[ ]:


#difference between args and kwargs 
##args = variable length arguements, its values depends upon context
##kwargs = keywords length arguements 


# In[26]:


#first classs functions vs high order functions , functions those can be assigned to a variable


def greeting():
    print(greeting)


# In[34]:



def addNo(num):
    print("hey")
    return "Tushar"


# In[35]:


out=addNo(10)
print("function returned:",out)


# In[36]:



def addNo(num):
    print("hey")
    return 500

out=addNo(100)
print("function returned:",out)


# In[41]:


#return can be used once. No statement will be executed after first return statement. 


def addno(a,b):
    sum=a+b
    return sum


# In[43]:



x=addno(10,20)
print(x)


# In[51]:


#high order funtion => if we pass a function as a arguement to another function is called high order function 


def salmankhan():
    print("dabang movie")
    
def aamirkhan(x):
    print("pk" ,x)
    
aamirkhan( salmankhan() )


# In[53]:


def salmankhan():
    return "dabang movie"
    
def aamirkhan(x):
    print("pk" ,x)
    
aamirkhan( salmankhan() )


# In[54]:


def salmankhan():
    return "dabang movie"
    
def aamirkhan(x):
    print("pk" ,x)
    
aamirkhan( salmankhan )


# In[56]:


def salmankhan():
    return "dabang movie"
    
def aamirkhan(x):
    print("pk" ,x())
    
aamirkhan( salmankhan )


# In[60]:


def square(x):
    print (x**2)

def Newfunction(num, func):
    print(num, func)

Newfunction(100,square(3) )


# In[61]:


###high order function 

def square(x):
    return x**2

def Newfunction(num, func):
    print(num, func(num))

Newfunction(5,square )


# In[ ]:


# # # ## Q1 read about high order vs first class
# # # ## Q2 create a function to take value and check the datatype 

# # #  --- If the datatype is int then create the number raise to the power of second number and return the value 
        
# # # ##Q3 create a function taking a string as a input 
# # #         if the word in the string contain any vowel remove the word from the string 


# # Q4 Take a input as string if the word contain letter "a" and "e" then adding "ing "in the last of the word otherwise add letter 
# "RA" at the starting of the word 

# # Q5 create square and pyramid(patterns)

# Q6 Take 2 input from the user as parameter and find its LCM of two numbers and return the lcm of both the numbers

#Q7 Find the HCF of two number n return the value

#Q8 Blog on Linkedin => about High Order vs first class 
#Q9 Exception Handling minimum of 200 words without chatgpt and AL tool/google


# In[1]:


#First class functions: If a function can be assigned to a variable or passed as object/variable to other function, 
#that function is called as first class function.


# The “first-class” concept only has to do with functions in programming languages. First-class functions means that the 
#language treats functions as values – that you can assign a function into a variable, 
#pass it around etc. It’s seldom used when referring to a function, such as “a first-class function”. It’s much more 
#common to say that “a language has/hasn’t first-class function support”.So "has first-class functions" is a property of a 
#language.

# Properties of first class functions:

# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists etc.
# So, languages which support values with function types, and treat them the same as non-function values, 
#can be said to have "first class functions".


# In[ ]:


# Higher-order functions are functions that work on other functions, meaning that they take one or more functions as an argument and can also return a 
# function.

# One of the consequences of having first class functions is that you should be able to pass a function as an argument 
# to another function. The latter function is now "higher order". It is a function that takes a function as an argument.

#Higher-order functions are only possible because of the First-class function


# In[25]:


#create a function to take value and check the datatype

def power_of_int(value1, value2):
    if isinstance(value1, int):
        result = value1 ** value2
        return result
  

value1 = 3
value2 = 3
print(power_of_int(value1, value2)) 


# In[46]:



#Q3 create a function taking a string as a input 

# #if the word in the string contain any vowel remove the word from the string 

def remove_vowels(string):
    words = string.split()
    nonvowel_words = [word for word in words if not any(vowel in word for vowel in ('a','e','i','o','u','A','E','I','O','U'))]
    result=nonvowel_words
    return result

string = "My name is Akansha Agrawal"
remove_vowels(string)
print(result)


# In[58]:


# # Q4 Take a input as string if the word contain letter "a" and "e" then adding "ing "in the last of the word otherwise add letter 
# "RA" at the starting of the word 


def update_word(string):
    words = string.split()
    updated_words = []

    for word in words:
        if 'a' in word or 'e' in word:
            updated_words.append(word + 'ing')
        else:
            updated_words.append('RA' + word)

    return ' '.join(updated_words)

string = "My name is Akansha Agrawal"
result = update_word(string)
print(result)


# In[62]:


def squared_stars(rows, cols):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * cols)
        else:
            print('*' + ' ' * (cols - 2) + '*')

rows = 4
cols = 4
squared_stars(rows, cols)


# In[65]:


def triangle_stars(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '* ' * i
        print(spaces + stars)

rows = 4
triangle_stars(rows)


# In[66]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_lcm():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = lcm(num1, num2)
    return result


lcm_result = find_lcm()
print(f"The LCM of the two numbers is: {lcm_result}")


# In[69]:


def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf_result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf_result}")


# In[ ]:




