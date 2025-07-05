# map(): Transform Each Item
# Higher order function
# Applies a function to every element in an iterable.
# Returns a map object (convert to list for display).
# Great for applying transformations like formatting, math, or string operations.


def cube(x):
    return x**3
print(cube(2))

# find cube of every element in list

# using for loop
l = [2,3,4,6,5,3]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)

# using map():
l2 = [2,3,4,6,5,3]
newl2 = list(map(cube,l2))  #map(cube,l2) -->this will return map object
print(newl2)


# map() + lambda: Transform Elements
# Applies a lambda function to each item in an iterable.

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16, 25]