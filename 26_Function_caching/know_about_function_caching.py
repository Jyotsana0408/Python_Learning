# Function caching/memoization -->
# way to store the results of expensive function calls so that if the same inputs are used again, 
# the result can be returned instantly—without recalculating. This technique is also called memoization.

# Why Use Function Caching?
# Speeds up repeated computations.
# Saves memory and CPU cycles.
# Great for recursive functions, API calls, or data processing.

# Use Caching When…
# Your function runs multiple times with the same input.
#   Example: Calculating Fibonacci numbers, factorials, or prime checks.
# Your function is expensive or slow.
#   Like API calls, web scraping, or database queries.
# You need faster performance without changing logic.
#   Caching can reduce processing time significantly without altering results.
# Results are always the same for given inputs.
#   This is key—if output may vary due to external factors (like time or randomness), caching won’t be reliable.

# Avoid Caching When…
# Function output changes frequently for the same input.
#   Example: get_weather("Bengaluru") might return different results every hour!
# Function involves randomness, time, or external data.
#   Functions using random(), time.now(), or APIs with live data shouldn't be cached unless results are stable.
# Memory usage needs to be minimal.
#   Large caches can eat up memory—use small maxsize or avoid entirely in constrained environments.
# Input types aren't hashable.
#   Caching relies on hashable inputs (like strings, numbers, tuples). Lists or dictionaries as arguments will break it.

# Built-in Tools for Caching

# 1. @functools.lru_cache
# Stores results of recent function calls using a Least Recently Used (LRU) strategy.
# maxsize: Limits how many results to store.
# typed=True: Treats 3 and 3.0 as different inputs.

# @functools.cache (Python 3.9+)
# Simpler version of lru_cache with unlimited size.




from functools import lru_cache
from functools import cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*2

print(fx(4))
print("Done for 4")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

# didn't compute again , stored the results
print(fx(4))
print("Done for 4")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

print(fx(8))
print("Done for 8")


@cache
def square(n):
    print(f"Calculating square of {n}")
    return n * n

print(square(4))  # First call calculates
print(square(4))  # Second call uses cache
