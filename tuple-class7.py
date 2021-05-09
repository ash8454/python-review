##Tuple
"""
A tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets.

#tuple are in round bracket and list are in square bracket
"""

#creating tuple
this_tuple= ("apple","banana","cherry")
print(this_tuple)


#Accessing tuple items
#you can access tuple items by referring to the index number, inside square brackets
print(this_tuple[1])


#range - you can specify range of indexes to get the tuple item
print(this_tuple[1:2])


#you cannot change tuple item value
#x=tuple(1,2,4)
# x[0]=3
# print(x)



#loop through a tuple
for x in this_tuple:
    print(x)


#check item in tuple
if "apple" in this_tuple:
    print("Item Present")


#find length of the tuple
print(len(this_tuple))

#join two tuple
tuple1= ("a","b")
tuple2 = ("c","d")
tuple3= tuple1 + tuple2
print(tuple3)

#remove tuple completely
tuple1 = ("a","b","c","d","e")
del tuple1



