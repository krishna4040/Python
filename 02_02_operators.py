# operators

# 1.arithmetic operators
print("The value of 3+4 is",3+4)
print("The value of 3-4 is",3-4)
print("The value of 3x4 is",3*4)
print("The value of 3/4 is",3/4) 
print("The value of quotionet when 3 divided by 4 is",3//4)
print("The value of remainder when 3 diveded by 4 is",3%4)
# / gives float as a result rest all(+-*//%) gives int as a result with integers only
# advanced math operations can be performed by math module

# 2.Assingment operators
a = 34
a += 2
a -= 2
a *= 2
a /= 2
print(a)
# vimp for recursive programes

# 3.comparison operators
b = (4>7)
b = (4<7)
b = (4>=7)
b = (4<=7)
b = (4==7)
b = (4!=7)
print(b) # gives boolean result

# 4.Logical operators: and,or,not
# operate on two booleans and results also in boolean
bool_1 = True
bool_2 = False
print("The value of bool1 and bool2 is",bool_1 and bool_2)
print("The value of bool1 or bool2 is",bool_1 or bool_2)
print("The value of  not bool1 is",not bool_1)

# 5.membership operator: is ,is not
# 6.identity operator: in, not in
# 7.bitwise operator: & | ~ <<(l) >>(r)