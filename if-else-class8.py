#if else
a = 3
b = 200
if b > a:
    print('b is greater than a')

#if-elif-else

a = 36
b = 33
if b > a:
    print('b is greater than a')
elif b == a:
    print('b and a are equal')
else:
    print('a is greater than b')


#short hand if else
c = 30
d = 21
if c > d: print('a is greater than b')

#short hand if elif
e = 31
f = 25
print("e is greater than f") if e > f else print("f is greater than e")


#three conditions
a = 330
b = 330
print('A') if a > b else print("=") if a == b else print('B')



#grade
grade = 3.3
if grade >= 3.5 and grade <=4.0:
    print("A grade")
elif grade >= 3.0 and grade < 3.5:
    print("B grade")
elif grade >= 2.5 and grade < 3.0:
    print("C grade")
elif grade >= 2.0 and grade < 2.5:
    print('D grade')
else:
    print("Failed")


#or condition
amount=500000
age = 70

if age >= 70 or amount >=1000000:
    print("you can retire now")
else:
    print("You still need to save some money")



#nested if
x = 15
if x > 10:
    print("Above ten")
    if x > 20:
        print("Above 20")
    else:
        print("Not above 20")


#printing no content

a = 33
b = 200
if b > a:
    pass #does not print anything or throws error


