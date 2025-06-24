

l = [1,2,3,4,5]
print(l)

# append method - add element
l.append(6)
print(l)

# sort method - to sort list
l2 = [11,3,66,5,4]
print(l2)

l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)

# reverse method -->reverse original list
l.reverse()
print(l)

# index method --> return index of element first occurence of list item
print(l.index(2))

# count method --> count the number of items
lst3 = [1,2,2,2,3,4,4]
print(lst3.count(2))

# copy method
# don't do this mistake  -->it will change original list
# m = l
# print(l)
# print(m)
# m[0] = 0
# print(l)

m = l.copy() #copy method
# print(m)
m[0] = 0
print(m)
print(l)

# insert method
l.insert(1,77)
print(l) #[6, 77, 5, 4, 3, 2, 1]

# extend method
a = [900,1000,1100]
l.extend(a)
print(l)  #[6, 77, 5, 4, 3, 2, 1, 900, 1000, 1100]

# concatenation

k = lst3 + a
print(k)

# remove method  - remove by value
lst4  = [2,3,4,5,6]
print(lst4)
lst4.remove(4)
print(lst4)

# del keyword - remove by index
lst5 = [1,3,5,7,9]
del lst5[2]
print(lst5)

# pop method - 
lst6 = [3,4,5,6,7]
removed_items = lst6.pop(2)
print(lst6)
print(removed_items)

# clear method - delete entire list
lst7 = [4,5,6,7,8]
lst7.clear()
print(lst7)