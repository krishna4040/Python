# string is a datatype in python

# difference between string and numeric literal (difference of quotes)
a = 34
b = "krishna"
print(a,b)
print(type(a),type(b)) 

# type of strings
'''
there are three types of strings
1.single quoted 
2.double quoted --> use this when ' in string
2.triple quoted --> use this when '" in string or for multiline strings
'''

# operations in strings 
'''
Arithmetic operations in string
1.concatenation + only with another string literal
2.multiplication * only with numeric literal
'''
name = "krishna"
sirname = "jain"
print(name+sirname) # concatenation
print(name * 10)    # multiplication
# print(sequence_type1 + sequence_type2) typeerror
# print(sequence + numeric )             typeerror
# print(a*float)                         typeerror


# string functions
# very useful for writing useful programs
story = "   once upon a time there was a youtuber harry who uploaded python course with notes   "
print(len(story))                                   # returns length of string as int
print(story.endswith("notes"))                      # returns boolean result
print(story.count("a"))                             # returns count of character or word in int
print(story.capitalize())                           # capatlize first word of string
print(story.find("once"))                           # returns index of first occurence of word in int
print(story.split())          ##vimp##              # convert components of string into a list we can take input from user in string then assign it in a list in a var. it ignores all white spaces in a string
print(story.strip())                                # remove whitespaces from both side of string
print(story.lstrip())
print(story.rstrip())
print(story.replace("Harry","code with harry"))     # replace given word with all occurences in a string 
                                                    # very useful for writing templates


# writing a template letter
letter = '''
Dear <|Name|>,
greetings from ABC coding house, I am happy to tell you about your selection
You are selected!
Have a great day

Date: <|Date|>
'''
name = input("Enter your name:")
date = input("Enter date:")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)