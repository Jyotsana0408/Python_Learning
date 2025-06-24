# update method
emp = {
    1: 65,
    2: 58,
    3: 89,
    4: 34,
    5: 90
}

emp1 = {
    6:56,
    7:78
}

emp.update(emp1)
print(emp)

# clear method  -- to remove all the items in dict
dict1  = {
    1:"amar",
    2:"amit",
    3:"ajay"
}

print(dict1)
dict1.clear() #will delete items not dictionary, will return empty dictionary
print(dict1)

# pop method
dict2  = {
    1:"amar",
    2:"amit",
    3:"ajay"
}

dict2.pop(2)
print(dict2)

#  popitem method - remove last item
dict2.popitem()
print(dict2)

# del keyword

dict3 = {
    1:"ajay",
    2:"neha",
    3:"raj"
}

# del dict3
# print(dict3) --> will delete whole dictionary with items

del dict3[3]
print(dict3)

