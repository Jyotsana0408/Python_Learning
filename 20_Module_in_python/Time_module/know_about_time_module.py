# The time module 
# lets you work with time-related tasks like measuring durations, delaying execution, and formatting timestamps.
# It’s part of the standard library, so no installation needed—just import time

import time

def usingWhile():
    i = 0
    while i<50:
        i = i+1
        print(i)


def usingFor():
    for i in range(51):
        print(i)

# time.time()
# Returns the current time in seconds since the epoch (Jan 1, 1970).

# time taken by for loop
init = time.time()
usingFor()
print("----------------------------------")
t1 = time.time() - init
print(t1)

# time taken by while loop
init = time.time()
usingWhile()
print("----------------------------------")
t2 = time.time() - init
print(t2)


# time.sleep(seconds)
# Pauses execution for the given number of seconds.

print("----------------------------------")
print(4)
time.sleep(3)
print("This is printed after 3 seconds")

# time.localtime([secs])
# Returns a struct_time object in local time.

# time.strftime(format, t)
# Formats a struct_time into a string.

t = time.localtime()
print(t)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time) # Output - 2025-07-07 11:24:55