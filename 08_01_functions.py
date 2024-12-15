# Functions: to avoid repetetion of same logic we use functions and group same logic
# defining a function
'''
def fun_name(argumentsittake(optional)):
    return value

def fun_name(arguments it take(optional)):
    var = value
    return var

def fun_name(arguments it take(optional)):
    var = value
    print(var)
'''
# funtion calling
'''func_name(parameters)'''
# Types of function --> 1.Built in  2.User defeined

# simple example
def greet(name):
    print(f"good day, {name}")
greet("krishna")

# Default Parameter value: this is used if we want no error when no parameter is passed in calling of function
def greet(name="default"):
    print(f"good day, {name}")
greet("krishna")
greet()


#programme to compare 3 numbers
def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is greatest")
    if b>a and b>c:
        print(f"{b} is greatest")
    if c>a and c>b:
        print(f"{c} is greatest")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
print(f"{greatest(num1,num2,num3)}")

# programme to convert c to f
def temp(celcius):
    farehnite = (celcius*9/5)+32
    return farehnite
celcius = int(input("Enter temp in celcius: "))
print(f"temprature in farehnite is {temp(celcius)} F")

# decreasing star pattern
def star(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        n = n-1
        print()
n = int(input("Enter n: "))
print(star(n))