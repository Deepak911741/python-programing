with open("practice.txt", "w") as f:
    f.write("hi every\nwe are learning File I/0\n")
    f.write("using java.\n I like progrmming in java")
    
new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)
    
word = learning
with open("practice.txt", "r") as f:\
    data = f.read()
    if(data.find(word) != -1):
        print("find")
    else:
        print("not find")
        
        
def check_for_line():
    word = "pyq"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
            
    return -1
print(check_for_line())
        