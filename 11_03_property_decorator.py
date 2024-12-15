# property decorator: when we want to convert a method as attribute we use @property before defining it '
# we call the function not as it is a function but as it is a attr and use all prop of attr
# attr_method have two decorators --> 1.getter  2.setter
# simple example:
class Employee:
    company = "bharatgas"
    salary = 5600
    salarybonus = 500
    # totalsalary = 6100
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary = 34
print(e.salarybonus)