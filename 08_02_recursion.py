# Recursion: it utilises the beauty of mathmatics(Telescoping series). In this function calls itself
# note1: recursion is used when function is decreasing. but if it is increasing then it calls itself infinately and stack overflows
# note2: recursion is v.useful sometimes in complex DSA

# factorial programme in different ways
n = int(input("Enter a number: "))

# method1
product = 1
for i in range(n):
    product = product * (i+1)
print(f"Result of method1 {product}")

# method2
def factorial_iter(n):
    product = 1
    for i in range(1,n+1):
        product = product * i
    return product
f = factorial_iter(n)
print(f"Result of method2 {f}")

# method3
'''logic:n!=(n-1)!*n!'''
def factorial_recur(n):
    if n == 1:
        return 1
    return n * factorial_recur(n-1)
f = factorial_recur(n)
print(f"Result of method3 {f}")


# programme to find sum of n natural number
def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)
n = int(input("Enter number: "))
print(f"sum of {n} natural numbers is {sum(n)}")
print(f"By formula (n*(n+1))/2 {(n*(n+1)/2)}")