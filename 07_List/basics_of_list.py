"""
- List are ordered collection ofdata items
- they store multiple items in single variable
- Lists are mutable
"""

l = [1,2,3,4,5,6]
print(l)
print(type(l))

# indexing of list - indexing starts from 0
# length of list - length starts from 1
print(l[0])
print(l[1])
print(l[2])

# can store any data type
l2 = [1,"one",1.0,False]
print(l2)

# Negative index
print(l[-3])  # negative index
print(l[len(l)-3])  #convert to positive index


# check if given element is present in list or not--> use in (same applies for string)
if 2 in l:
    print("yes") #print "yes"
else:
    print("no")


if "2" in l:
    print("yes")
else:
    print("no") #print "no"

# list slicing
print(l[:]) #[1, 2, 3, 4, 5, 6]
print(l[1:-1]) #[2, 3, 4, 5]
print(l[1:4])  #[2, 3, 4]
print(l[1:4:2])  #[2, 4] -->jump index -->[start:end:jump]


# list comprehension
lst = [i for i in range(4)]
print(lst)

lst1 = [i*i for i in range(4)]
print(lst1)

lst3 = [i*i for i in range(10) if i%2==0]
print(lst3)