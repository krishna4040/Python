# keywords -- reserved words cannot be used as variables
# variable as container variables are same as dns to ip
# datatype -- prakar type of data(AKA literals)
a = int
a = "krishna"       # 1.strings 
b = 345             # 2.integer 
c = 45.32           # 3.float   
d = 5E01            
e = 1+2j            # 4.complex 
f = None            # 5.none    
g = True            # 6.Bollean  
h = 6>4            
i = [1,"h"]         # 7.list    
j = (1,"h")         # 8.tuple   
k = {1:"h",2:"k"}   # 9.dict    
l = {1,2,"k"}       # 10.set    

'''
var naming rules
1.alplhabet digit special symbol
2.start with alphabate _
3.keywords,whitespaces,starting with digit not allowed 
'''

# keep in mind: var naming is case sensitive

'''
vimp: triple quotes is used for writing
1.multiline comments
2.strings in multiple line(within print as well as variable)
'''

# printing variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)

# print type of a variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))