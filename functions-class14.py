#Functions

"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""

#Creating a function
def my_function1():
    print("Hello from a function")

my_function1()


#functions with arguments
def my_function2(fname):
    print(fname + " Tulachan")

my_function2("Ashok")
my_function2("Avanna")
my_function2("Max")


#more than one arguments
def my_function3(fname, lname):
    print(fname + " " + lname)

my_function3("Ashok", "Tulachan")



#if you don't know no of args, you can use *args
def my_function4(*kids):
    print("The youngest child is " + kids[2])

my_function4("Avanna", "Alana", "Avril")



"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.
"""

def my_function5(**kid):
    print("His last name is: " + kid["lname"])

my_function5(fname="Tobias", lname="dash")


#Default Parameter value:
#You can use default value as well
def my_function6(country= "US"):
    print("I am from: "+country)

my_function6()
my_function6("Nepal")


#Passing a list as an argument

"""
You can send any data types of argument to a function (string, number, list,
 dictionary etc.),and it will be treated as the same data type inside the function.
"""

def my_function7(food):
    for x in food:
        print(x)

my_function7(["apple", "banana", "orange"])


#Return value = you can return value as well
def add(x, y):
    return x + y

print(add(2,5))
print(add(20000,100))



###Recursion
"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

"""

def tri_recursion(k):
    if (k > 0):
        print("K in here" +str(k))
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example results")
tri_recursion(6)