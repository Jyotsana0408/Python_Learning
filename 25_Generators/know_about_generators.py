# generators are a way to create iterators that yield values one at a time, only when needed—making them memory-efficient 
# and perfect for handling large or infinite data streams.

# Analogy --->
# Think of a generator like a vending machine
# It gives you one snack at a time when you press the button, instead of dumping all the snacks at once.
# In Python, generators give you one value at a time, only when you ask for it—so they’re memory-friendly.

# What Makes Generators Special?
# They use the yield keyword instead of return.
# They pause after each yield, saving their state.
# They resume from where they left off when next() is called.

# Generator vs Regular Function
# -------------------------------------------
# Feature	    Regular Function	    Generator Function
# Returns	    One final value	        Multiple values over time
# Memory usage	High (stores all data)	Low (yields one at a time)
# Syntax	    return	                yield


def my_generator():
    for i in range(5):
        yield i

# yield sends one number out, then pauses.
# next() asks for the next number.
# It’s like saying: “Give me the next item!” instead of “Give me everything now!”

gen = my_generator()
# print(next(gen)) -->0
# print(next(gen)) -->1
# print(next(gen)) -->2
# print(next(gen)) -->3


for j in gen :
    print(j) # 0 1 2 3 4
