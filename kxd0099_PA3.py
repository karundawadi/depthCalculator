# Name : Karun Dawadi 
# Net ID : kxd0099
# Student ID : 1001660099
# Date turend in : 11/30/2020

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
    if("{" in i or "}" in i):
        if(i.find("//")!=-1 or i.find("\"")!=-1):
            # Using regex here
            j = i
            # Replaces all the values inside the "" with a whitespace
            val_regex = "\".+\""
            j = regex_val.sub(val_regex," ",j)

            # Means that sentence consists of \\ or " mark 
            # Using the relative position from the \\ to see if we need to count it or not
            # Since \\ would mean a complete line 
            if(i.find("{")<i.find("//") and j.find("{")!= -1): # Means that if { comes before an \\ sign 
                # If this is inside " then we need to ignore it 
                depth = depth +1

            if(i.find("}")<i.find("//") and j.find("}")!= -1): # Means that if } comes before an \\ sign 
                # If this is inside " then we need to ignore it 
                depth_carry = depth_carry - 1
            
        else:    
            if(i.find("(")!= -1 and i.find("}") != -1):
                # Meaning both exist in a single line 
                continue # Since both means that the depth is temporary and should not be counted 
            
            if(i.find("{")  != -1):
                depth = depth + 1
            
            if(i.find("}") != -1):
                depth_carry = depth_carry - 1     

    print(f"{depth} {i}")
    # Since we took } as depth_carry subtracting that and setting that to zero, for next rotation
    depth = depth + depth_carry 
    depth_carry = 0  