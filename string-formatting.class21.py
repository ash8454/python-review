#String formatting
"""
The format() method allows you to format selected parts of a string.

"""

price = 49
quantity = 3
itemno = 567
txt = "The price is {} dollars"
txtDouble = "The price is {:2f} dollars"
txtMultiple= "I want {} pieces of item {} for {} price"
print(txt.format(price)) #print int value
print(txtDouble.format(price)) #print double value
print(txtMultiple.format(quantity,itemno,price))



#You can use index numbers (a number inside the curly brackets {0}) to be sure the 
# values are placed in the correct placeholders:
txtIndex= "I want {0} pieces of item {1} for {2} price"
print(txtIndex.format(quantity, itemno, price))


#You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names 
# when you pass the parameter values txt.format(carname = "Ford"):

txtIndex = "I have a {carname}, it is a {model}"
print(txtIndex.format(carname = "Ford", model="Mustang"))