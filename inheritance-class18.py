##Inheritance

"""
Inheritance allows us to define a class that inherits all the methods and properties 
from another class.

Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.


"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)


#user person class to create an object
x = Person("John", "Doe")
x.printname()



#create child class
class Student(Person):
    pass #print no content

#create new object
y = Student("Mike", "Olsen")
y.printname()


#create child class with different parameter

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
    
    #methods
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationYear)


#create new object
z = Student("Mike", "Nappi", 2019)
z.printname()
z.welcome()