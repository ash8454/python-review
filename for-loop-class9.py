#For Loop - A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


#since string is array of characters, you can loop easily as well
name = "ashok"
vowel_count = 0
for x in name:
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print('Got vowel word: '+x)
        vowel_count+= 1

print(vowel_count)


#use break statement if you want to exit out early

#find first vowel letter
name = "ashok"
vowel_count = 0
for x in name:
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        print("Vowel found")
        vowel_count+=1
        break
print(vowel_count)


#continue: we can stop the current iteration of the loop
#and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


#range() = Loop through set of a code a specified number of times
for x in range(6):
    print(x) # print 0..5 excluding 6

for y in range(2,6):
    print(y) #print (2 to 5) excluding 6


# you can increment the value by adding 3 parameter as well
for x in range(1,10,2):
    print("Number" +str(x)) #print only even value till 100


#Nested loops
adj= ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#you can use pass to print no content
for x in [0, 1, 2]:
    pass

