# Inheritance is way of creating new class from existing class
# Types of inheritance --> 1.single  2.multiple  3.multilevel


# 1.single inheritance
'''
class class_parent:
    class_attr
    method and var
class class_child(class_parent):
    class_attr
    method and var
object_parents = class_parent()
object_child = class_child()
'''
# note1: object_parent can call only class_parent attr and methods
# note2: object_child can call class_parent as well as class_child attr and method
# note3: if both class have same attr or method and object_child calls one of them then attr and methods of class_child are prefferd or priorised

# simple employee example:
class Employee:
    company = "google"
    def showdetail(self):
        print("this is an employee")
class programmer(Employee):
    language = "python"
    def getlan(self):
        print(f"language is {self.language}")
    def showdetail(self):
        print("this is an programmer")

e = Employee()
e.showdetail()
print(e.company)
# e.getlan()
# print(e.language)
print("------------")
p = programmer()
p.showdetail()
p.getlan()
print(p.company)
print(p.language)


# 2.Multiple inheritence:
'''
class class_father:
    body
class class_mother:
    body
class class_child(father,mother):
    body
'''
# note: to father to mother priority of same attr and methods dec. i.e. father is priorised over mother 
# simple Employee example
class Employee:
    company = "visa"
    ecode =120
class Freelancer:
    company = "fiver"
    level = 0
    def upgradelevel(self):
        self.level = self.level+1
class programmer(Employee,Freelancer):
    name = "rohit"

p = programmer()
p.upgradelevel()
print(p.level)
print(p.company)
print("---------")


# 3.Multilevel inheritence
'''
class class_grandparent:
    body
class class_parent:
    body
class class_child:
    body
'''
# note1: priority of child is father and grandfather
# note2: priority of child is father when there is compt b/w father and grandfather
# simple example
class person:
    country = "India"
    def takebreath(self):
        print("I am taking breath.....")
class Employee(person):
    company = "honda"
    def getsalary(self):
        print(f"slary is {self.salary}")
    def takebreath(self):
        print("I am an emplyee so i am also breathing....")
class programmer(Employee):
    company = "Fiverr"
    def getsalary(self):
        print("No salary to programmers")
    def takebreath(self):
        print("I am an programmer so i am breathing python....")

p = person()
p.takebreath()
print(p.country)
# print(p.company)
e = Employee()
e.takebreath()
print(e.company)
print(e.country)
pr = programmer()
pr.takebreath()
print(pr.company)
print(pr.country)

# super: if we want to run methods of father_class to run in child_class
# simple example:
class person:
    country = "India"
    def takebreath(self):
        # super().takebreath()
        print("I am taking breath.....")
class Employee(person):
    company = "honda"
    def getsalary(self):
        print(f"slary is {self.salary}")
    def takebreath(self):
        print("I am an emplyee so i am also breathing....")
        super().takebreath()
class programmer(Employee):
    company = "Fiverr"
    def getsalary(self):
        print("No salary to programmers")
    def takebreath(self):
        print("I am an programmer so i am breathing python....")
        super().takebreath()

p = person()
p.takebreath()
e = Employee()
e.takebreath()
pr = programmer()
pr.takebreath()