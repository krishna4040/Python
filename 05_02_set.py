# sets --> collection of non repetetive values
a = {1,2,3,4,5,1}
b = {}      # this creates an empty dictionary and not an empty set
c = set()   # this create empty set  
d = {18,'18',18.0}

# printing sets
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

# properties of sets
'''
1.unordered(no indexing)
2.item assingment is not possible(immutable)
3.duplicate entries allowed but not printed
'''


# Set methods or functions
# c.add(value)               # add value to set ##list and dict is not hashable(immutable) hence not supported in values##
# c.remove(item)             # remove item from set
print(len(a))                # do not includes duplicate entry in len
print(a.pop())               # remove arbitrary element
print(a.clear())             # empties the set
print(a.union({6,7,8,8}))    # just maths
print(a.intersection({1,2})) # just maths