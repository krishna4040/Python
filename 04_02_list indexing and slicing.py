# list indexing --> 1.positive  2.negetive
a = [1,2,4,56,6]
print(a[0])
print(a[-1])
# print(a[5]) index error
# nested indexing
b = ["apple",45,45.76,'krishna']
print(b[0][3])
print(b[-1][-3])


# item assingment is allowed in list
a[0] = 23
print(a)
a[2] = a[3]
print(a)


# List slicing
# # slicing --> name[start:stop:jump]
# slicing proceed from    1.moving forward:start to stop-1    2.moving backward:start to stop+1
freinds = ["harry","tom","Rohan","sam","Divya",45]
print(freinds[0:4])
print(freinds[-4:])