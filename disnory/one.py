# info = {
#     "key" : "values",
#     "Name" : "Deepak",
#     "learning" : "coading"
# }


# print(info)
# print(type(info))

# Dictinory are used to store data values in key:value paries
# They are unorderd, mutable(chngeble) & don't allow dublicate keys


# info = {
#     "key" : "values",
#     "Name" : "Deepak",
#     "learning" : "coading"
# }


# info["Name"] = "Kumar"
# info["surname"] = "Pandit"
# print(info)


# null_dict = {}
# null_dict["Name"] = "Deepak"
# print(null_dict)


student = {
    "name" : "Deepak",
    "score" : {
        "chem" : 98,
        "phy" : 85,
        "math" : 74
    }
}

# print(len(list(student.keys())))

# print(student.values())

# print(student.items())
print(student["name2"]) # error
print(student.get("name2")) # no error -> None


