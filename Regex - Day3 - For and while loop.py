#!/usr/bin/env python
# coding: utf-8

# In[1]:


##### loop -->  For repetive task 

#for loop => for certain values 


#number of iteration is known  ---- for loop 
# number of iteration is unknown ----while loop 


# # for loop with range (start, stoping , step =1)
# 
# for i in range(0,5):
#     print(i)

# In[2]:


#var[0:5:1]


for i in range(0,5,1):
    print(i)


# In[3]:


for i in range(5,1,-1):
    print(i)


# In[4]:


#for loop on data is called iterator 


for i in "hey":
    print(i)
    
#dir("hey") => _iter_method


# In[5]:


#len(), to calculate the length of the string 


x="hey12233"
len(x)


# In[6]:


x="hey12"
count=len(x)
len(x)
for i in range(0,len(x)):   
    print(i,x[i])


# In[7]:


for num in range(0,11):
       if(num%2==0):
        print(num)


# In[8]:


for num in range(1,51):
    if(num%2==0 and num%3==0):
        print(num)


# In[9]:


str = "akansha"
for i in str:
    if(i in "aeiou"):
        print(i, "we have a vowel")


# In[10]:


#take a input from a user and find out how many total vowels are present 
#take a input from a user and find out how many individual vowels are present 
#take a input from a user and find whether "a" and "e" both are present in the string or not
#take 3 values(length, breadth,height) as input from the user 
#---- if user provide 1=> area of traingle 
#---- if 2=> area of square 
#-----if 3 => rectangle 
#-----if 4 take input and find area of circle


# # while loop 
# 

# In[11]:


index=0
while(index<10):
    print(index)
    index=index+1
    


# In[15]:


str="akansha"
index=0
while(index<len(str)):
    print(str,str[index])
    index=index+1


# In[26]:


n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# # assignment 

# In[3]:


##Q1 Take a input from the user and find oout how many total vowels are present

user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"

vowel_count = 0

for char in user_input:
    if char in vowels:
        vowel_count += 1

print("Total vowels:", vowel_count)


# In[1]:


##Q3 Take a input from the user and find whether "a and e" are both present in the string or not

user_input = input("Enter a string: ")

if 'a' in user_input and 'e' in user_input:
    print("Both 'a' and 'e' are present in the string.")
else:
    print("Either 'a' or 'e' or both are not present in the string.")


# In[4]:



#Q2 Take a input from the user and find out how many individual vowels are present

user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"

vowel_count = {vowel: 0 for vowel in vowels}

for char in user_input:
    if char in vowels:
        vowel_count[char] += 1

print("Individual vowel counts:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")


# In[2]:


# Q4 Take three ( length, breath, height) value as input from the user and find out
# - if user provide 1 => area of triangle
# - if 2 => area of square
# - 3 => area of rectangle
# - 4 => take input and find area of a circle



import math

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side * side

def calculate_rectangle_area(length, breadth):
    return length * breadth

def calculate_circle_area(radius):
    return math.pi * radius ** 2

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))
choice = int(input("Enter choice (1: Triangle, 2: Square, 3: Rectangle, 4: Circle): "))

if choice == 1:
    area = calculate_triangle_area(length, height)
    print("Area of triangle:", area)
elif choice == 2:
    area = calculate_square_area(length)
    print("Area of square:", area)
elif choice == 3:
    area = calculate_rectangle_area(length, breadth)
    print("Area of rectangle:", area)
elif choice == 4:
    radius = length  # Using length to store the radius value
    area = calculate_circle_area(radius)
    p
    rint("Area of circle:", area)
else:
    print("Invalid choice. Please enter a valid choice.")


# In[ ]:




