#SETS

"""
A set is a collection which is unordered and unindexed. 
In Python sets are written with curly brackets.
"""
this_set = {"apple", "banana", "cherry"}
print(this_set)


#accessing item from the set
'you cannot access items from set using index since it is unordered'
'but you can use loop to get the item from the set'
this_set = {"apple", "banana", "cherry"}
for x in this_set:
    print(x)

#check item is present in the set
print('banana' in this_set)


#add_items
#use add method to add item in the set
this_set = {"apple", "banana", "cherry"}
this_set.add("pineapple")
print(this_set)


#use update to add multiple items in the set
this_set.update(["orange", "mango", "grapes"])
print(this_set)


#get the length of the set
print(len(this_set))


#remove item from the sert
this_set.remove("orange")
print(this_set)


#remove last item from the set
x = this_set.pop()
print(x)
print(this_set)


#clear method empties the set:
set1 = {"apple", "banana", "cherry"}
set1.clear()
print(set1)

#delete set items
del set1

#join two sets by using union which gets both items from both list
set1 = {"apple", "banana", "cherry", "apple"}
set2 = {"orange", "mango", "grapes"}
set3 = set1.union(set2)
print(set3)


#update method - inserts the item in set2 to set1
set1 = {"a","b","c"}
set2 = {1,2,3,"a"}
set1.update(set2)
print(set1)

#get unique items from two list
l1 = [1,2,3,4]
l2 = [5,6,3,8]
l3 = set()
for x in l1:
    print("Itemx:" +str(x)) #get item from x
    for y in l2:
        print("Itemy:" +str(y)) #get item from y
        if x != y: #check if x is equal to y
            l3.add(y) #check if it is not, add y
            print(l3) #print y
    if x != y:
        l3.add(x)
        print(l3)
print(l3)

#get common items from two list
l1 = [1,2,3,4]
l2 = [5,6,2,3]
l3 = set()
for x in l1:
    print("Itemx:" +str(x)) #get item from x
    for y in l2:
        print("Itemy:" +str(y)) #get item from y
        if x == y: #check if x is equal to y
            l3.add(y) #check if it is , add y
            print(l3) #print y
    if x == y:
        l3.add(x)
        print(l3)
print(l3)


#gets the difference between two lists
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", 'apple'}
z = x.difference(y)
print(z)