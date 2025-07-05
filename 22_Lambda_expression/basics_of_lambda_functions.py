# A lambda function  --->
# small, anonymous function defined using the lambda keyword. 
# It's perfect for short, throwaway operations—especially when you don’t want to formally define a function using def


# Syntax ---> lambda arguments: expression
# You can pass any number of arguments, but only one expression.
# The result of the expression is automatically returned.

# When to Use
# Use Case	                ||   Why Lambda Works Well
# Short, one-time functions	||   No need for def
# Functional programming	||   Works with map, filter, reduce
# Inline operations	        ||   Keeps code concise


# def double(x):
#     return x*2


double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x,y:(x+y)/2
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(double(5))
print(cube(5))
print(avg(4,8))
print(check(7))
print(check(8))

def appl(func, value):
    return 6 + func(value)

print(appl(lambda x: x*x, 4))
