# oops: object oriented programming
# This helps in code reusability. It implements DRY(do not repeat yourself) principle

# procedural oreinted programming
a = 12
b = 34
print(f"the sum of a and b is {a+b}")
# oops:
class number:
    def sum(self):
        return self.a + self.b
num = number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

# class:class is custom layout which can create an object. it act as blank form with template. it is always wrriten in pascalcase not in camelcase
# object: it is instatntaion of class. it act a filled form
# using oops to a problem
'''
1.noun:class --> Employee
2.adjective:attributes --> name,age,salary
3.verb:methods --> getsalary(),income()
'''
# syntax:
'''
class class_name:
    class_Attributes = "info"
    methods and variable
class_name.class_attribute = "we can change this by this"
object = class_name()  
object.object_attribtue = "info"
print(object.object_attribute)
print(object.class_attribute)
object.method()
'''
# note1: if object_attribute and class_attribute are same then object_attribute is priorised. new obj attribute is created for that particular object but class attribute do not change
# note2: if we try printing a object.attribute that is not created either as a object_attribute nor as a class_attribute then it throws attribute error
# note3: object = class_name():this line act as filling a form and creating a object.
# note4: object.method():this gives one argument(object) to specified method defenied inside class. 

# simple railway application example:
class Railwayform:
    formtype = "Railway form"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"train is {self.train}")

harrysapplication = Railwayform()
harrysapplication.name = "harry"
harrysapplication.train = "Rajdhani express"
harrysapplication.printdata()

# simple employee example:
class Employee():
    company = "google"
    salary = 100

harry = Employee()
krishna = Employee()
krishna.address = "hathras"
harry.salary = 300
a = krishna.company  # class_attribute
b = krishna.salary   # class_attribute
c = krishna.address  # object_attribute
d = harry.salary     # object as well as class attribute
# e = harry.mobile   # thows attribute error becauz this do not exist
print(a,b,c,d)


# railway ticket booking
class train():
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getstatus(self):
        print("*************")
        print(f"The name of train is {self.name}")
        print(f"The seats available in train is {self.seats}")
        print("*************")
    def fareinfo(self):
        print(f"The price of the ticket is Rs.{self.fare}")
    def bookticket(self):
        if self.seats>0:
            print(f"your ticket is booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Train is full! please try in tatkal")

intercity = train("Intercity express 14015",90,2)
intercity.getstatus()
intercity.fareinfo()
intercity.bookticket()
intercity.getstatus()


# calculator by oops:
class calculator():
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")
    def squareroot(self):
        print(f"The value of {self.number} square root is {self.number**0.5}")
    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")
    def cuberoot(self):
        print(f"The value of {self.number} cube root is {self.number**(1/3)}")

a = calculator(3)
a.square()        
a.squareroot()
a.cube()        
a.cuberoot()
print("----------")
b = calculator(5)
b.square()        
b.squareroot()
b.cube()        
b.cuberoot()