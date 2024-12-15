# modules
# inbuilt and external
# pip is used to install external modules
# python as REPL vs IDE
# python as calculator we use REPL
# we use IDE to write large code 
# comments -- pound symbol & triple comments
# single line(inline and starting of line) and multiline comments
'''
this is 
a multiline comments
'''

print("hello world")
'''
print("twinkle twinkle
little star how i wonder
what you are")               #completely wrong
'''
# vimp: we use triple quotes inside print to print string in multiline

# Printing a poem in multiline 
print('''
twinkle twinkle little star
how i wnder what you are 
up above the sky so high
like a dimond in the sky
''')


# importing a inbuilt module and using it
import os  
print(os.listdir())

import math as m        # as aliasis
print(m.sqrt(49))


#importing a external module and using it
from playsound import playsound 
playsound("/home/krishna/Downloads/test.mp3")