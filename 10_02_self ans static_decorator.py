# writing methods or functions in class 
'''
class class_name():
    class_attr = ""
    def func_name(a):
        body
        print("any text")
        print(self.class_atrr)
        print(self.obj_atrr)
    @staticmethod
    def func_name():
        body
object = class_name()  
object.object_attribue = "info"
object.method()
'''
# self: it is simple parameter. but we use "self" word becauz it is always understood with class.it take object as argument.
# why self: when we call obj.method() it coverts it to class.method(obj).Hence one argument is given automatically  
'''obj.method() == class.method(obj)''' # hence if self is not passed in method_def then it gives argument error.
# @staticmethod: when conversion is not requiered. when we want to stop automatic giving of argument.
'''object.method() == class.method()'''


# simple Employee example
class Employee():
    company = "google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("good day sir")
harry = Employee()
harry.salary = 100000
harry.getsalary()
harry.greet()

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
    @staticmethod
    def greet():
        print("****welcome to the best calculator of the world****")

a = calculator(3)
a.greet()
a.square()        
a.squareroot()
a.cube()        
a.cuberoot()
print("----------")
b = calculator(5)
b.greet()
b.square()        
b.squareroot()
b.cube()        
b.cuberoot()