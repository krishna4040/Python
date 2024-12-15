# lists --> is a ordered sequence of comma seprated character
# we use [] for list
# we can create a list with item of different types
a = [1,2,4,56,6]
b = ["apple",45,45.76,'krishna']
# list is printed alongwith []
print(a)
print(b)


# operations on tuples
print(a+[1,2,3,4])
print(a*2)              
# print(sequence_type1 + sequence_type2) typeerror
# print(sequence + numeric )             typeerror
# print(a*float)                         typeerror


# list methods or functions
l1 = [1,8,7,2,21,15]
# these functions are not printed directly or assingend to another var they are directly used
# l1.sort()               # sorts the list
# l1.reverse()            # reverse the list
# l1.append(item)         # adds at the end of the list  #######vimp######
# l1.insert(index,item)   # adds item to given index
# l1.pop(index)           # delete element at given index
# l1.remove(item)         # delete given element
# print(sum(l1))          # print sum of list element expection we can even assign it to var
l1.append(23)
print(l1)
print(sum(l1))