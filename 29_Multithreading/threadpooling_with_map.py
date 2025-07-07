# ThreadPoolExecutor.map() ---> 
# powerful and elegant way to run a function across multiple inputs concurrently using threads—similar to Python’s built-in map(),
# but with parallel execution.

# How It Works
# executor.map(task, iterable) applies task() to each item in the iterable.
# All tasks run in parallel using threads (up to max_workers).
# Results are returned in the same order as the input iterable—even though tasks finish at different times.

# Key Differences from submit() --->
# Feature	        submit()	                    map()
# Returns	        Future object	                Direct results (iterator)
# Result order	    May vary (use as_completed)	    Preserved from input iterable
# Flexibility	    More control over each task	    Simpler for uniform tasks


import time

from concurrent.futures import ThreadPoolExecutor

def task(n):
    print(f"Sleeping for {n} seconds")
    time.sleep(n)
    return f"Finished {n}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [3, 2, 1])

for result in results:
    print(result)
print("---------------------------------------------------")

# You can use zip() to pass multiple arguments:
def greet(name, delay):
    time.sleep(delay)
    return f"Hello {name} after {delay}s"

names = ["Jyotsna", "Alex", "Riya"]
delays = [2, 1, 3]

with ThreadPoolExecutor() as executor:
    results = executor.map(greet, names, delays)

for r in results:
    print(r)

