#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Student_Register:
    sid=10
    sName="tushar"


# In[2]:


#object = classname(), Object will always have charaterstics as well as functionalities or behaviour will be defined 
#through a function 

s1=Student_Register()  


# In[11]:


print(s1.sid, s1.sName)


# In[14]:


class Student_Register:
    sid=10
    sName="tushar"
    
    def register(self):
        print("hello student iss register")
    
s2=Student_Register()  
print(s2.sid, s2.sName)

s2.register()


# In[23]:


#s1=>sid s2=>sid
#constructor-method => which will initialize the memory for the object 

class StudentRegister:
    def __init__(self):
        print("hey user",self)
        
s1=StudentRegister() 
print(s1)

#paranthesis is for telling that constructor is working.Self is keyword which holds the memory address of current object.
#see the memory address of object and self is same.
#whenever an object is created, new memory address is created.


# In[24]:



class StudentRegister:
    def __init__(self):
        print("hey user",self)
        
s1=StudentRegister(10) 
print(s1)


# In[32]:



class StudentRegister:
    
    def __init__(self,num):
        self.sid=num          #self will make global variable
        print("hey user",self.sid)
        
s1=StudentRegister(10) 
        
s2=StudentRegister(15) 


# In[46]:


class employee:
    
    def __init__(self,id,name):
        self.e_id=id
        self.e_name=name
        
    def employeeInfo(self):
            print(self.e_id,self.e_name)
              
emp1=employee(2,"xyz")
emp1.employeeInfo()


# In[47]:



class Driver:
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
        
    def info(self):
        print("Info is :", self.id,self.name,self.email)


# In[48]:


d1=Driver(11,"aman","aman@gmail.com")


# In[49]:


d1.info()


# In[58]:



class Employee:
    def __init__(self,eid,ename,eemail,wallet):
        self.eid=id
        self.ename=name
        self.eemail=email
        self.wallet=wallet
        
    def info(self):
        print("Info is :", self.eid,self.ename,self.eemail,self.wallet)


# In[61]:


#e1=employee(11,"tushar","tushar@gmail.com",)


# In[ ]:


#inheritance => to remove the duplicacy from the code 

#parent class /Superclass
#Child Class /Subclass/derived class


# In[63]:



class Driver:
    amount=100
    
    def Info(self):
        print('Driver class')


# In[66]:


class Employee(Driver):
  salary=500

e1=Employee()
e1.Info()


# In[70]:


class Driver:
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
        
    def info(self):
        print("Info is :", self.id,self.name,self.email)


# In[73]:



class Employee(Driver):
    def __init__(self,eid,ename,e_email,wallet):
        super().__init__(eid,ename,e_email)
        self.wallet=wallet
    
e1=Employee(99,"Aditya","aditya@gmail.com",990)

e1.id
e1.name
e1.wallet


# In[74]:


# create a class name as customer having id, name , salary and email Address as attributes/members. Now inherit customer class to 
#customer hobby class having the information id,name,hobby and print and all these information for the customer hobby class


# In[79]:


class Customer:
    def __init__(self,id,name,email,salary):
        self.id=id
        self.name=name
        self.email=email
        self.salary=salary
        
    def info(self):
        print("Info is :", self.id,self.name,self.email,self.salary)


# In[91]:


class Customer_Hobby(Customer):
    def __init__(self,cid,cname,cemail,csalary,hobby):
        super().__init__(cid,cname,cemail,csalary)
        self.hobby=hobby
    
c1=Customer_Hobby(99,"Aditya","tushar@gmail.com",15000,"Dance")

print(c1.id)
print(c1.name)
print(c1.hobby)


# In[ ]:


# multiple #multilevel inheritance 
# Inheritance is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by 
# deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties 
# from another class. 

#Benefits of inheritance are:

#Inheritance allows to inherit the properties of a class, i.e., base class to another, i.e., derived class. The benefits of
#Inheritance in Python are as follows:

# # It represents real-world relationships well.
# # It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add 
# # more features to a class without modifying it.
# # It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of 
# # B would automatically inherit from class A.
# # Inheritance offers a simple, understandable model structure. Less development and maintenance expenses result from
# # an inheritance. type of inheritance.

# There are 5 different types of inheritance in Python. They are as follows:

# Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an 
# example above.
# Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 
# Multilevel inheritance: When we have a child and grandchild relationship. This means that a child class will inherit from 
# its parent class, which in turn is inheriting from its parent class.
# Hierarchical inheritance More than one derived class can be created from a single base.
# Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one 
# type of inheritance.


# In[ ]:


#polymorphism 
#encapsulation 

