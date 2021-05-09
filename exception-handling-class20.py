###Exception handling
"""

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the
 try- and except blocks.
"""

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


#You can use else to print out other command
a = 10
b = 1

try:
    c=a/b
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")


#Finally - The finally block, if specified, will be executed regardless if 
# the try block raises an error or not.


try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


#try to open and write to a file that is not writable
# try:
#     f = open('demofile.txt')
#     f.write("Lorum Ipsum")
# except:
#     print("Something went wrong when writing to the file")
# finally:
#     f.close()


#Raise an exception 
"""
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
"""

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below 0")

#raise type error
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers is allowed")

x="ashok"
if not type(x) is str:
    raise TypeError("Only string is allowed")
else:
    print("No error")