# Input function --> to take input from user
a = input("Enter your name")
print(a)
print(type(a)) # it always take input as string literal

# we use typecasting to take input in numeric literals
b = int(input("enter number:"))
print(b)

# Taking input from user and performing and combining basic operations:
x = int(input("Enter num1:"))
y = int(input("Enter num2:"))
print("sum of num1+num2 is",x+y)
print("avg of num1 and num2 is",(x+y)/2)


# print --> to show the output of programme
# properties of print
'''
1.we can print multiple things at a time by sep them by commas which are printed line by line.
2.we use f strings--> f"thisisstring {thisisvariable}" application: you do not need to use commas. use "fstr" custom snippet. we can print two f strings at the same time.
3.we use end="anything"
4.we use sep="anything"
'''
a = input("Enter your name: ")
print(f"your name is {a}")
print(1,2,"krishna",23.4,[1,"krishna"],end="*****",sep="@@@@@")
print(f"this was a custom f string")
