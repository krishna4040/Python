# string indexing
# string is "sequence" of character enclosed in quotes and sequences have indexing 
# indexing is done using []
# Types of indexing
'''  
1.positive:index start from 0 to len-1
2.Negetive:index start from -1 to -len
'''
name = "krishna"
print(name[4]) # printing indvidual character of string sequence
# print (name[7]) --> give index error
# name[6] = "fgg" --> item assingment not supported in string sequence


# principle of string slicing:
# slicing --> name[start:stop:jump]
# slicing proceed from    1.moving forward:start to stop-1    2.moving backward:start to stop+1
'''1.moving forward'''
print(name[1:3])
print(name[:3])    # same as [0:3:1]
print(name[1:])    # same as [1:len+1:1]
print(name[-4:-1]) # same as [3:6:1]
print(name[1:3:2])
'''2.moving backward''' # we have to always use -ve jump value to print oterwise it does not print
print(name[5:1])
print(name[-2:-6:-1])
print(name[6:0:-1]) 
