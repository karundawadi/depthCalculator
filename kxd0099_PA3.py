# Name : Karun Dawadi 
# Net ID : kxd0099
# Student ID : 1001660099
# Date turend in : 11/30/2020

import os as operting_system

# Reading the file
test_file = open("input.txt",'r')
try:
    # All the contents of the file are transfeered to a list file_contents
    file_contents = test_file.readlines()
finally:
    test_file.close()

# File read complete 
# Printing the contents of the file 
for i in file_contents:
    print(i)
