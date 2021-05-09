###Python Classes/Objects

"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""

#example of class
class MyClass:
    x = 5

#create object
p1 = MyClass() #creates object named p1 from MyClass
print(p1.x) #prints out x value


#init_function
""""
The __init__() Function
The examples above are classes and objects in their simplest form,
 and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed 
when the class is being initiated.

Use the __init__() function to assign values to object properties, or other 
operations that are necessary to do when the object is being created:

"""


'The self parameter is a reference to the current instance of the class,' 
'and is used to access variables that belongs to the class.'

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age


p1 = Person("John", 36)
print(p1.name) #prints name
print(p1.age) #prints age


#Object Methods
"""
 Objects can also contain methods. Methods in objects are functions that belong to the object.
 Let us create a method in the Person class:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Jacob", 36)
print(p1.name)
p1.myfunc()

#modifying object properties
p1.age = 40
print(p1.age)

#delete object properteis
del p1.age
