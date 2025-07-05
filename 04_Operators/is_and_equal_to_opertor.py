# == checks for value equality
# It asks: “Do these two objects have the same value?”
# Even though a and b are different objects in memory, their contents are equal.

# is checks for identity
# It asks: “Are these two variables pointing to the exact same object in memory?”

# Use == when comparing values.
# Use is when checking for identity—especially with None:

a = 4
b = "4"

print(a is b)  # exact location of object in memory --> False
print(a == b)  # value ---> False

d = 4
c = 4

print(c is d)  # True
print(c == d)  # True

l1 = [1,2,3]
l2 = [1,2,3]

print(l1 is l2) #False
print(l1 == l2) #True

