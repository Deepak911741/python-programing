# Block of statement that perform a specific task.

# def calcu(a, b):
#     sum = a + b
#     print(sum)
#     # return sum

# calcu(10, 20)
#     #
# calcu(20, 50)
#     #
# calcu(30, 40)   


#function defination
# def clacu(a, b): #parameters
#     return a + b

# sum = clacu(178, 200) #function call; argument
# print(sum)


# def print_hello():
#     print("Hello")
    
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
    
    
# def print_hello():
#     print("Hello")
    
# output = print_hello() #None
# print(output)


def cal_culat(a, b, c):
    sum = a + b + c
    avg = sum / 3
    # print(avg)
    return avg

cal_culat(87, 20, 98)


# function types in python 

# 1) Built-in Function(print, len, type, range)           2) User defined Function(khud se difind kare o hamra user defined Function kahlata hai)


cities = ["delhi", "gurugaon", "noida","pune", "mumbai", "chenni"]
heroes = ["thor", "ironman", "caption", "saktiman"]

def println(list):
    print(
        len(list)
    )

# println(cities)
# println(heroes)


# def print_list(list):
#     for item in list:
#         print(item, end=" ")
        
# print_list(heroes)
# print()




# def cal_fal(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
        
# cal_fal(6)

def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
    
convert(73)