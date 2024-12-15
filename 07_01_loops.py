# loops
# types of loops -->1.while   2.for

# while loop:
# syntax -->
'''
var declaration
while boolean:
    body of loop
    updation
'''
# condition is checked if it is true then loop runs if false it is ignored
# simple example:
i = 0
while i<10:
    print("yes"+str(i))
    i = i+1
print("done")


# for loop
# syntax -->
'''
for var in sequence:
    body of loop
'''
# range function --> for number sequence we use range function in sequence. ##range(start,stop,jump)## ###move from start to stop-1###
# simple example1:
for x in "krishna":
    print(x)
# simple example2:
for i in range(1,8,2):
    print(i)


# looping + conditional statement 
# while-else and for-else
# simple example
for i in range(10):
    print(i)
else:
    print("this is inside else of for")


# multiplication programme
a = int(input("Enter a number to get its multiplication table: "))
b = int(input("Enter a number till where multiplication is requiered: "))
for i in range(b+1) :
    multiply = a*i
    print(f"{a} x {i} = {multiply}")

# factorial programe:
a = int(input("Enter number whose factorial is req: "))
factorial = 1
for i in range(1,a+1):
    mul = i
    factorial = factorial * mul
print(f"factorial of {a} is {factorial}")