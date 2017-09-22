# -*- coding: utf-8 -*-
"""
Create the US flag by using nested for loops.

Usage:
    /.make_flag.py

Author: 
    Mira Kajo - 22.9.2017
"""
# Extra (optional) exercise to create a US stars and stripes flag using nested for loops and conditional statements.

# Create the variables for the start part of the flag:
star = '*'
text = ''

# Create the variables for the stripes of the flag:
line = '-'
flag = ''

# Create the nested for loop for US flag:
for x in star:
    for y in range(3):
        text = x * 7
        #print(text)
        if text == '*******':
            text = text + line * 12
            print(text)
    for y in line:
        for f in range(2):
            line = y * 19
            print(line) 
            

            
        
       
