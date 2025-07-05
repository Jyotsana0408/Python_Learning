# filter()--->
# Higher order function
# Select Items That Match a Condition
# Filters elements based on a Boolean function.
# Keeps only items where the function returns True.
# Ideal for cleaning data or extracting subsets.


l = [2,3,4,6,5,3]

def filter_func(a):
    return a>3

newl = list(filter(filter_func,l)) # by printing filter(filter_func,l) you will get filter object
print(newl)


# filter() + lambda: Select Matching Items
# Keeps only items that satisfy a condition.

# python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]