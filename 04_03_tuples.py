# Basic tuples
# we use () for tuple
a = (1,2,3,4,5)
b = ()
c = (1,)    #for single element we need to use ,

# printing elements of tuples
print(a)
print(b)
print(c)


# basic difference bw tuples and lists
# tuples do not support item assingment while list does
# a[1] = "krishna" throws typeerror


# operations on tuples
print(a+(1,2,3,4))
print(a*2)
# print(sequence_type1 + sequence_type2) typeerror
# print(sequence + numeric )             typeerror
# print(a*float)                         typeerror


# tuple functions
t = (1,2,4,5,1,1,2)
print(t.count(1))
print(t.index(5))