# Python can be used to perform operations on a file
# Open, Read & close File 

f = open("text.txt", "r")
data = f.read()
print(data)
print(type(print))


# Reading a file

# data = f.read()  #reads entire file
# data = f.readline() #reads one line at a time

f = open("text.txt", "r")
data = f.readline()
print(data)
print(type(print))



# Writing to a file 

f = open("text.txt","w")
f.write("this is a new line") #overwrites the entire file


f = open("text.txt", "a")
f.write("this is a new file") # adds to the file


# with Sysntax 

with open("text.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("text.txt", "r") as f:
    f.write("new data")
    
    
# Deleting a File 

# using the os module 

# Module(like a code library) is a file written by another programmer that generlly has a function we can use.

import os
os.remove("text.txt")
    
