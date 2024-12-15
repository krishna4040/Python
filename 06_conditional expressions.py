# conditional expressions
# when we have to take decision which depend on condition met
# IF ELSE ELIF 


# operators useful with conditional expressions:
'''
1.Relational operators: ==,!=,<,>,<=,>=
2.Logical operators: or, and, not 
3.membership operator: is ,is not
4.identity operator: in, not in
'''


#syntax
'''
if(condition1):
    corrosponding statement
elif(condition2):
    corrosponding statement
else:
    corrosponding statement
'''

# simple example1:
a = 45
if a>3:
    print("value is greater than 3")
elif a>13:
    print("value is greater than 13")
elif a>15:
    print("value is greater than 15")
else:
    print("value is not greater than 3 ,15 nor 15")
# note1: if-elif-else ladder is followed line by line
# note2: to check all conditions instead of elif use if each time
# note3: there can be any number of elif statements
# note4: else is otherwise it works when all conditions fails
# note5: else statement is optional

# simple example2:
age = int(input("Enter your age"))
if age>34 and age<56:
    print("you can work with us")
else:
    print("you cannot work with us")