# Custom error

# l = [1,2,3]
# i = int(input("Enter index: "))

# if i>=0:
#     # l = [1,2,3]
#     # i = int(input("Enter index: "))
#     print(l[i])
# else:
#     raise IndexError("Index can't be less than zero")


# Handle index error

l1 = [1,2,3]
i1 = int(input("Enter index: "))

try:
    # l = [1,2,3]
    # i = int(input("Enter index: "))
    print(l1[i1])
except Exception as e:
    print(e)
    

