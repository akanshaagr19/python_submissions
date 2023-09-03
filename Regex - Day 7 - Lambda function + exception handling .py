#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##function,type of arguement , first class vs high order 
#map , filter , lambda function 



# lambda, keyword is used 
# anonymous function 
# # default return 

# def name
# lambda ( no name here)

# lambda para1,param2 : expression


# In[1]:


def square(num):
    return num**2
square 


# In[4]:


xyz = lambda num: num**2


# In[6]:


xyz(10)


# In[7]:


# def square(num):
#     return num**2

# mylist=[10,20,30,40]

# for data in mylist:
# #     square(data)


# In[11]:


# map function => pick every individual element 
# apply function => returns values

#iterables - on which loop can be run 
#iter_ - used to retrive the value

##using simple function 

def square(num):
    return num**2

mylist=[10,20,30,40]
list(map(square,mylist))


# In[12]:


##using lambda function 

mylist=[10,20,30,40]

list (map(lambda num : num**2,mylist))


# In[16]:


def even_odd(num):
    if (num%2==0):
        return num 
num=[3,4,5,7]
list(filter(even_odd,num))


# In[17]:


## when we apply split on a string, it rerturns a list always

mylist=["hey tushar","raj here"]

list (map(lambda x : x.split(" "),mylist))


# In[28]:


#exception handling 
#try - except 

try:
    x=10
    print("tushar")
    x/0
    print("hey")
    
except Exception as err:
    print("error generated",err)


# In[29]:


try:
    x=10
    print("tushar")
    x/xxxx
    print("hey")
    
except NameError as err:
    print("error generated",err)


# In[30]:


#if error class name is defined,program must have a related error otherwise it will not be able to handle the exception 


try:
    x=10
    print("tushar")
    x/0
    print("hey")
    
except NameError as err:
    print("error generated",err)


# In[33]:


try:
    x=10
    print("tushar")
    x/kkk
    #x/0
    print("hey")
    
except NameError as err:
    print("error generated",err)
    
except ZeroDivisionError as err:
    print("error generated",err)
       


# In[36]:


try:
    x=10
    print("tushar")
    x/kkk
    #x/0
    print("hey")
    
except (NameError,ZeroDivisionError) as err:
    print("error generated",err)
    


# In[38]:


#exception will handle all the error which are not known at the starting 


try:
    x=10
    print("tushar")

    print("hey")
    
except (NameError,ZeroDivisionError) as err:
    print("error generated",err)
except Exception as err:
    print("error generated",err)


# In[40]:


try:
    x=10
    try: 
        x/0
    except:
        print("error here")
    
    print("hello user")
    print("hey user")
    
except:
    print("### Error found here ##")


# In[41]:


#else and #finally statements:

#else startment will run if there is no error in the code
try:
    x=10
    x/0
except:
    print("error")
    
else:
    print("hey user")


# In[43]:


#finally will run always if the code has a error or not 

try:
    x=10
    x/0
except:
    print("error")
    
finally:
    print("hey user")


# In[44]:


##raise statement is used to generate the error explicitly

try:
    x=10
    if(x%2==0):
        raise ValueError
    else:
        print(x)
    
except ValueError:
    print("Error is")


# In[ ]:




#type hinting - We give the hint to a user of a datatype of a variable as well as the datatype of return as well


# In[48]:


#file handling: this is a mechanism where we can take the input and give output to access later

#file_obj = open("filename","access-modifier")
#r(read),w(write),a(append)


fileobj=open("regex.txt","r")
x=fileobj.read()
fileobj.close()

print(x)


# In[50]:



fileobj=open("regex.txt","w")
#x=fileobj.read()
x=fileobj.write("hey")
fileobj.close()

print("hey")


# In[53]:


#content gets overwritten from the first position in r+ but if it starts with other position then first it 
#will go to the last position 

fileobj=open("regex.txt","r+")
x=fileobj.write("hey")
x=fileobj.read()

fileobj.close()

print("hey####")


# In[56]:


#content gets flushed first then start writing

fileobj=open("regex.txt","w+")
x=fileobj.write("hey&&")
x=fileobj.read()

fileobj.close()

print("hey@@")


# In[57]:


#content gets written at the end of the file's content=

fileobj=open("regex.txt","a+")
x=fileobj.write("ion")
#x=fileobj.read()

fileobj.close()

print("hey@@")


# In[1]:


#tell and #seek method 

fileObj=open("regex.txt","a+")

print( fileObj.tell() )

fileObj.seek(2)
print( fileObj.tell() )
x=fileObj.read(3)

print( fileObj.tell() )
fileObj.write("$$$")
print("After write", fileObj.tell() )
fileObj.close()
print(x)





# # Learning Assignment 
# 
# #Exception vs error
# #Why syntax error can not be handled in python 
# #read vs readline method
# #file handling => second method (with keyword)
# #life scope of variabels (Global,local,exposed)
# #variable inside the fucntion
# 
# 
# #try to download the youtube video 
# 

# In[ ]:


# Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 
# Two types of Error occurs in python. 

# Syntax errors
# Logical errors (Exceptions) 


# In[ ]:


# The Python file read() function allows us to read an entire file at once and store it in a string. Depending on the size of your file, this could make sense for you
# and your application.

# readline() can be useful if you are doing processing and just want to access particular line.


# In[ ]:


#  File handling in Python is simplified with built-in methods, which include creating, opening, and closing files.

# # While files are open, Python additionally allows performing various file operations, such as reading, writing, 
#and appending information.


# In[4]:


# Python Global variables

#Global variables are the ones that are defined and declared outside any function and are not specified to any function.
#They can be used by any part of the program.

#Local variables are those that are initialized within a function and are unique to that function. It cannot be accessed 
#outside of the function.


# In[ ]:


# In Python, variables defined inside a function are typically considered local variables, meaning they have scope only within
# that specific function.Local variables are typically used for temporary storage within a function and are not accessible
#from other parts of code. 


# In[12]:


pip install youtube-dl


# In[13]:


import subprocess

# URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=He1JvqbFED4"

# Specify the command to run youtube-dl
command = ["youtube-dl", video_url]

try:
    # Run the command
    subprocess.call(command)
    print("Download complete!")
except Exception as e:
    print("An error occurred:", str(e))


# In[ ]:




