# ProcessPoolExecutor() is a class from Python’s concurrent.futures module that 
# lets you run functions in parallel using multiple processes
# perfect for CPU-bound tasks like data crunching, image processing, or simulations.

# executor.map() applies the square() function to each item in the list in parallel.
# Each task runs in a separate process, bypassing Python’s Global Interpreter Lock (GIL).

# Why Use It?
# Feature	            Benefit
# True parallelism	    Uses multiple CPU cores
# GIL-free execution	Great for CPU-heavy tasks
# Simple API	        Easy to use with map() or submit()
# Automatic pooling 	Manages process lifecycle for you


from concurrent.futures import ProcessPoolExecutor

def compute(n):
    return n * n

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute, [1, 2, 3, 4])
        for r in results:
            print(r)
