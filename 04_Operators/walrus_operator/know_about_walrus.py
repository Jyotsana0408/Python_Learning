# The walrus operator (:=) in Python --->
# Assign values to variable as a part of larger expression
# is a handy feature introduced in Python 3.8 that lets you assign a value to a variable as part of an expression
# saving you from writing repetitive code.

# Syntax ---> variable := expression
# This assigns the result of expression to variable and returns the value.

# Use Cases

# Context	            Example
# while loops	        while (line := f.readline()):
# if statements	        if (n := len(data)) > 0:
# List comprehensions	[name for entry in data if (name := entry.get("name"))]



# Without walrus operator
my_list = [1,2,3,4,5,6,7,8]
value = len(my_list)
if value > 5:
    print(value)


# With walrus operator
if (value := len(my_list)) > 5:
    print(value)


a = True
# print(a =False)  TypeError: print() got an unexpected keyword argument 'a'
print(a :=False)


# walrus operator with while loop
numbers = [1,2,3,4,5]
while(n := len(numbers)) > 0:
    print(numbers.pop())

foods = list()
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)


# walrus operator with list comprehension
data = [{"name": "Jyotsna"}, {"name": "Munmun"}, {"name": None}]
names = [name for entry in data if (name := entry["name"])]
print(names)  # Output: ['Jyotsna', 'Munmun']


# walrus operator with function call
def get_data():
    print("Fetching...")
    return [1, 2, 3]

if (result := get_data()):
    print("Got:", result)



