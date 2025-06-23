# Tuples are ordered collection of data items 
# tuples are mutable

tup = (1,2,3,4)
print(tup)
print(type(tup))

# one element tuple
tup1 = (1) #int
print(tup1)
print(type(tup1))

tup2 = (1,) #tuple
print(tup2)
print(type(tup2))

# tuples are immutable or unchangeable

# tup3 = (1,2,4)
# tup[0] = 1  --->this will throw error tuples are immutable but lists are immutable

# access elements of tuple

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

print(tup[-1]) # negative index

# check if item is present or not
if 2 in tup:
    print("Yes")

# slicing in tuple will return new tuple
tup4 = tup[1:3]
print(tup4) # new tuple 

