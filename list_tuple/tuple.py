# tuples 

# A build-in data type taht lets us create immutable sequence of values

# list is the mutble 
# tuple is the immutble 


# tup = (5, 8, 9, 14, 45)
# print(tup)
# print(type(tup))


# tup = (5, 8, 9, 14, 45)
# print(tup[1:4]) # slicing [1:5] ye slicing hai
# # print(type(tup))


# tuple metods
 
# tup = (5, 8, 9, 14, 45)
# print(tup.index(8))


# tup = (5, 8, 9, 14, 45)
# print(tup.count(8))

# movies = []
# list1 = input("enter the first movie name : ")
# list2 = input("enter the second movie name : ")
# list3 = input("enter the third movie name : ")

# movies.append(list1)
# movies.append(list2)
# movies.append(list3)

# print(movies)


#palindrom the revese values is same 
#ex [10, 20, 30, 10] -> [10, 30, 20, 10]

# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# copy_list = list1.copy()
# copy_list.reverse()

# if(copy_list == list1):
#     print("palindrom")
# else:
#     print("NOT palindrom")


# grade check


# grade = ("C", "A","B", "F", "A", "B", "P", "A" )

# print(grade.count("A"))


# short order

grade = ["C", "A","B", "F", "A", "B", "P", "A" ]

grade.sort()
print(grade)    