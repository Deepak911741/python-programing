# set 

# Set is the collection of the unorderd items
# Each element in the set must be unique & immutable

# collection = {1, 2, 3, 3, 3, "hello", "world", "Deepak", 4}

# print(collection)
# print(len(collection))


# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)

# collection.remove(1)
# print(collection)


# collection = {"hello", "world", "deepak", "kumar", "pandit"}


# print(collection.pop())


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.union(set2)) #{1, 2, 3, 4}


# subject = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }

# print(len(subject))


marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter che : "))
marks.update({"che" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)