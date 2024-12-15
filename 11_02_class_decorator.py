# class method and static method are two decorators in class
# static method: used when we do not want argument not to be passed when an method is called by an object
# class method: when we created a class_attr and do not want to create same object_attr but update class_attr for some objects.
# we use class method to deal with class attributes only   
# simple example
class Employee:
    company = "camel"
    salary = 100
    location = "Delhi"
    @classmethod
    def changesalary(self,sal):
        self.salary = sal
e = Employee()
print(e.salary)
e.changesalary(455)
print(e.salary)
print(Employee.salary)