# file?
# file is solution of volatile memory of Ram which can store data and easily stored on aour rom
# Types of file ---> 1.Text files(can be opened in notepad)   2.Binary files(cannot be opened in notepad)

# Python provides functions to manipulate files on ROM
# syntax
'''
file_obj = open("file_name","mode(r,w,a,t)")

var1 = file_obj.read(no. of char)       # print specified data
var2 = file_obj.readline()              # print one line
var3 = file_obj.readline()              # print next line
file_obj.write("content to be added")   # updation method
file_obj.append("content to be added")  # updation method

print(var)
file_obj.close()
'''
# note1: open is an inbuilt function
# note2: by default mode is r
# note3: in mode value we specify t for text files and b for binary files like, rt and rb
# note4: by default read function reads complete file


# With clause --> it closes file automatically
'''
with open("file_name) as file_obj:
    var = file_obj.read()
    print(var)
'''


# simple example:
# reading contents of file
with open("sample.txt","r") as f:
    a = f.read()
    b = f.read(5)
    c = f.readlines()
    print(a,b,c)
# updating in write mode
f = open("sample.txt","w")
f.write("This is write content")
f.close()
# updating in append mode
f = open("sample.txt","a")
f.write("This is appended content")
f.close()