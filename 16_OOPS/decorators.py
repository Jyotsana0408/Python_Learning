# Decorators -->
# Decorators in Python are a powerful and elegant way to modify or extend the behavior of functions or methods
# without changing their actual code

# A decorator is a function that:
# Takes another function as input
# Wraps it with additional functionality
# Returns a new function
# This is possible because Python treats functions as first-class objects, meaning they can be passed around like variables.


def my_decorator(func):
    def wrapper(*args ,**kwargs):
        print("Good Morning!")
        func(*args, **kwargs)
        print("Thanks for using this function")
    return wrapper

@my_decorator  # modifying the existing hello()
def hello():
    print("Hello, World!")

@my_decorator
def add(a,b):
    print(a+b)

# all two will return same thing
hello()
# my_decorator(hello)()
add(1,2)
# my_decorator(add)(3,5)