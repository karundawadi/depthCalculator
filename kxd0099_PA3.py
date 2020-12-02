# Name : Karun Dawadi 
# Net ID : kxd0099
# Student ID : 1001660099
# Date turend in : 11/30/2020
# Operating system used MacOS 10.15

import os as operting_system
import re as regex_val

# Reading the file
test_file = open("input.txt",'r')
try:
    # All the contents of the file are transfeered to a list file_contents
    file_contents = test_file.readlines()
finally:
    test_file.close()

# File read complete 

# Defining the depth variable 
depth = 0
depth_carry = 0

# Printing the contents of the file 
for i in file_contents:
    j = i
    # Replace value inside "quotation marks" with Regex 
    val_regex = "\".+\""
    val_comment = "(//.*)"
    j = regex_val.sub(val_regex," ",j) # Replaces the values inside the quotation marks with a whitespace
    j = regex_val.sub(val_comment," ",j) # Replaces all the comments in the line with a whitespace, works as a comment line 
    # comment line menas no text after \\
    k = list(j)
    for n in k:
        if (n == '{'):
            depth = depth+1
        if (n == '}'):
            depth_carry = depth_carry - 1 # Since we need to delay the count

    print(f"{depth} {i}")
    # Since we took } as depth_carry subtracting that and setting that to zero, for next rotation
    depth = depth + depth_carry 
    depth_carry = 0  