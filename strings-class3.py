"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""
name = "Ashok Tulachan"
print(name[0])


#Slicing - You can return a range of characters by using the slice syntax
#Specify the start index and the end index separated by colon to return part of string
message = "Hello, World!"
print(message[2:5])


#Use negative indexes to start from slice from the end of the string
print(message[-5:-2])


#Use len() to get the length of the string
print(len(message))


#Built in Methods

#strip() = removes any whitespace from the beginning or the end
a = " Hello, World "
print(a.strip())


#lower() = returns the string in lower case
print(a.lower())


#upper() = returns the string in upper case
print(a.upper())

#replace() = replaces a string with another string
print(a.replace("H", "J"))

#split() = splits a string into substring if it finds instances of the separator
print(a.split(","))

#check = To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
y= "bin" not in txt
print(x)
print(y)


#Concatenation string and number using format() method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity=3
item_no=567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars"
print(my_order.format(quantity, item_no, price))
my_order2= "I want {2} dollars for {0} pieces of item {1}" #use index numbers to make sure the arguments are placed in
#correct order
print(my_order2.format(quantity, item_no, price))


#use escape character to insert characters that are illegal in a string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)