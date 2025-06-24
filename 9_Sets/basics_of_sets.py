# stes are unordered collection of data item
# set do not contain duplicate values
# sets are unchangeable ,  you can not change items once set is created(immutable)
# set cannot be accessed using index

s = {2,4,5,2,3,4,5,6,7}
print(s)

info = {"carla", 19, False, 5.8, 19}
print(info)

# create a empty set and print type of it
# empty_set = {}  ---> empty dctionary not set
empty_set = set()
print(type(empty_set))

# access set data items
for value in info:
    print(value)


