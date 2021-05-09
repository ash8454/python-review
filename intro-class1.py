print("Hello World")

if 5 > 2:
 print("Five is greater than two")


#variables
x = 5
y = "Hello World"

print(x)
print(y)

#multiline comments
"""
This is a multi comment 
more than one line
comment
"""
print("Multi line comment")

#string variable
name1= "John"
name2= 'Andrew'
print(name1)
print(name2)

#assign value to multiple variables
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("---------")
print(x,y,z)


#concatenation of string
first_name = "Ashok"
last_name = "Tulachan"
print(first_name + last_name)

#global variable - variable outside of function
x = "awesome"
def myfunc():
    print("Python is: " + x)

myfunc()


#local variable
def my_local_func():
    x= "amazing"
    print("Python is " + x)

my_local_func()


#variable with global keyword
x = "awesome"
def my_global_variable():
    global x
    x = "fantastic"
    print("Python is: " + x)

my_global_variable()


