"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

"""


#Get Type of variable
x = 10
name = "Ashok"
amount = 10.21
isAmerican = True

print(type(x))
print(type(name))
print(type(amount))
print(type(isAmerican))


#Python Numbers
x = 1 #int
y = 2.8 #float
z = 1j #Complex = Complex numbers are written with a "j" as the imaginary part:


print(type(x))
print(type(y))
print(type(z))

#conversion from int to float
a = float(x)
print(a)

#conversion from float to int
b = int(y)
print(b)

#conversion from int to complex
c = complex(x)
print(c)

#converting number to string
d = str(x)
print(d)
print(type(d))

#No random function but random module that can make random numbers
import random
print(random.randrange(1, 10))


#String literals
print("hello")
first_name = "Ashok"
last_name = "Tulachan"
print("My name is: " + first_name + " " + last_name)

