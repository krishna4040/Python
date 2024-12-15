# constructor

'''
class class_name():
    def __init__(self,parameter1,parameter2):
        print("This is constructor")
object = class_name(argument1,argument2)  
'''
# note: __init__() method runs itself whenver object is created

# simple example
class programmer():
    company = "microsoft"
    def __init__(self,name,salary,product):
        self.name = name
        self.salary = salary
        self.product = product
        
    def printdata(self):
        print(f"Name of programmer is {self.name}")
        print(f"Salary of programmer is {self.salary}")
        print(f"product of programmer is {self.product}")
        print(f"company of programmer is {self.company}")

harry = programmer("krishna",120000,"github")
Alka = programmer("alka",300000,"skype")

harry.printdata()
print("--------------------------------")
Alka.printdata()