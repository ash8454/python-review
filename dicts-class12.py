#Dictionary

"""
A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
"""

#create and print dictionary
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(this_dict)

#accessing items from the dict
x = this_dict.get("model") #using key
y = this_dict["model"]
print(x)
print(y)


#changing the value using key
this_dict["model"] = "taurus"
print(this_dict)


#loop through a dictionary

#print key one by one
for x in this_dict:
    print(x)

#prints all value sone by one
for x in this_dict:
    print(this_dict[x])

#use values
for x in this_dict.values():
    print(x)

#print both values
for x, y in this_dict.items():
    print(x, y)



#check if key exists
if "model" in this_dict:
    print("Yes", 'model is one of the key')


#get the length of the dicts
print(len(this_dict))


#Adding items in the list
this_dict["color"] = "red"
print(this_dict)

#removing item from the list
this_dict.pop("model")
print(this_dict)

#popitem() removes the last inserted item
x=this_dict.popitem()
print(this_dict)


#clear empties the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.clear()
print(this_dict)


#copy a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
copy_dict = thisdict.copy()
print(copy_dict)


#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

