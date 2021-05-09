#Lists- A list is a collection which is ordered and changeable. 
# In Python lists are written with square brackets.

this_list= ["apple","banana","cherry"]
print(this_list)


#you can access the list by the index number
print(this_list[0])

#Negative indexing means beginning from the end, -1 refers to the last item,
#  -2 refers to the second last item etc.

print(this_list[-1])


#Rnage of indexes 
# You can specify a range of indexes of specifying where to start and end the range
this_list= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5]) #from 2nd index to 5th index

print(this_list[:4]) # from first to 4th index
print(this_list[4:]) #from 4th to n-1 index


#change item value in list
this_list[1] = 'pinepapple'
print(this_list[1])

#looping through a list
for x in this_list:
    print(x)

print("Using range")
for i in range(len(this_list)):
    print(this_list[i])

#check if item exists
if "apple" in this_list:
    print("Yes", "Apple is in the list")

#get the length of the list
print(len(this_list)) #len gets the length of the list


#Add item in the list
#append() method adds in the list
list2 = ["ashok", "bina", "avanna"]
list2.append("max")
print(list2)

#insert item at certain position 
list3 = ["ashok", "max", "bina"]
list3.insert(1, "avanna")
print(list3)


#remove item from the list
list4 = [1,2,3,4]
list4.remove(3)
print(list4)


#pop removes the item at certain index or last element
list5 = [5,6,7,8]
list5.pop(1) #removes 1st index
print(list5)
list5.pop() #removes last element
print(list5)

#del keyword removes the specified index
list6=[10,11,12,13]
del list6[0]
print(list6)
# del list6
# print(list6) #throws error

#clear - empties the list
list7=["test","ashok"]
list7.clear()
# print(list7)
# list7[:]=[]
print(list7)

#copy a list
thislist = ["apple", "banana", "cherry"]
mylist=thislist.copy()
# mylist = list(thislist)
print(mylist)

#join two list 
#1 -using +
list1=["a", "b", "c"]
list2=[1,2,3]
list3=list1+list2
print(list3)


#2 - append list2 into list1 using for loop
for x in list2:
    list1.append(x)

print(list1)

#3- extend method to add list2 at the end of list1
list3=["a", "b", "c"]
list4=[1,2,3]
list3.extend(list4)
print(list3)


#Reverse the item from the list
list5 = ['apple','banana','cherry']
list5.reverse()
print(list5)


#create a new list
new_list=list(("ashok","avanna","bina"))
print(new_list)