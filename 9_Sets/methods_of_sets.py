s1 = {1,2,3,4,5,6}
s2 = {3,6,7}

# union method --> s1+s2(will include duplicates once only) 
print(s1.union(s2))
print(s1,s2) #set will remain unchange

# update method
s1.update(s2)
print(s1,s2)   #{1, 2, 3, 4, 5, 6, 7} original set will change(s1 will update)

s3 = {1,3,4,5,6}
s4 = {1,2,3}

# intersection method
print(s3.intersection(s4))

# intersection_update
s3.intersection_update(s4)
print(s3)


# symmetric difference  --> A union B - A intersection B
# values which are not common in both set

s5 = s3.symmetric_difference(s4)
print(s5)

# difference method (A-B)-->items only present in original set but not in both the sets
s6 = s3.difference(s4)
print(s6)

# <-----------methods to manipulate the sets ------------->

# isdisjoint()
# check if items are given is present in set or not
# have no element in common - no intersection

set1 = {1,2,3,4}
set2 = {5,6,7}
print(set1.isdisjoint(set2))


# issuperset method --> all the items of particular set is present in original set
set3 = {1,2,3,4,7,5,6}
set4 = {1,2,3}
print(set3.issuperset(set4))
print(set4.issuperset(set3))


# issubset method --> check if all the items of the original set are present in particular set

print(set3.issubset(set4))
print(set4.issubset(set3))


# add method --> add a item in set
my_movies = {"Great","Fire","Superman"}
my_movies.add("Power Rangers")
print(my_movies)

# remove/discard methods --> to remove or delete the item from the set

# remove will raise an error if item is not present in the set
# discard will not raise an error if item is not present in the set
my_movies.remove("Great")
print(my_movies)


# pop method -> removes the last item from set but remeber sets are unordered

set5 = {1,3,5,7,2,2,95,3,2}
item = set5.pop()
print(set5)
print(item)


# del method --> can remove entire set
set6 = {1,2,3,4,5}
# del set6
# print(set6) -->  throw error

# clear method --> will not delete set but items in the set

set7 = {12,4,6,8,4,3}
set7.clear()
print(set6)