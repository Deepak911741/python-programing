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
