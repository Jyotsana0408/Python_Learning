# The enumerate() function in Python is a built-in tool that makes looping with counters super easy and clean.
# Instead of manually tracking indexes with range(len(...)), enumerate() gives you both the index and the value in one go.
# return tuple


marks = [12,35,67,98,45,34]

for index,mark in enumerate(marks,start=1):
    print(mark)
    if (index == 3):
        print("You are using enumerate function")