# reduce(): Combine Items into a Single Value
# Higher order function
# Applies a function cumulatively to reduce an iterable to one result.

from functools import reduce

number = [1,2,3,4,5,6]

def my_sum(x,y):
    return x+y
sum = reduce(my_sum,number)
print(sum)

# reduce() + lambda: Aggregate to One Value
# Combines items cumulatively using a lambda function.
num = [1,2,3,4,5,6]
sum1 = reduce(lambda x,y: x+y,num)
print(sum1)
