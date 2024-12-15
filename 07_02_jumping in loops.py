# there are two jumping statements in loops:
'''
1.break
2.continue
3.pass statement
'''

# break: break is used to come out of loop when encountered
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("this is inside else of for")
# importance of for-else --> else statements only execute on succsesful termination of loop. it will not execute with break


# continue: use to avoid particular iteration. it returns to start of loop when it is encountered
for i in range(10):
    if i==5:
        continue
    print(i)
else:
    print("this is inside else of for")


# pass statement
# when pass is used significance of loop/conditional/function_def vanishes
# simple example1:
i = 4
if i > 0:
    pass
print("krishna is a coder")
# simple example2:
def sound(ouch):
    pass            # iss function ko badme complete krenge pr bhool na jaye iss liye pahele bna diya

# prime number programme
num = int(input("Enter number to be checked: "))
prime = True
for i in range(2,num):
    if num%i == 0:
        prime = False
        break
if prime:
    print(f"{num} number is prime")
else:
    print(f"{num} is not prime")