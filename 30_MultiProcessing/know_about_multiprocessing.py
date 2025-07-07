# Multiprocessing in Python is a technique that lets you run multiple processes in parallel, 
# making full use of your CPU cores—especially useful for CPU-bound tasks like data crunching, image processing, or simulations.

# Why Use Multiprocessing? ---->
# Python’s Global Interpreter Lock (GIL) limits true parallelism in threads. 
# But with multiprocessing, each process runs in its own Python interpreter, bypassing the GIL and unlocking real parallel execution 1 2.

# Process(...) creates a new process.
# .start() begins execution.
# .join() waits for the process to finish.

# Multiprocessing vs Multithreading --->

# Analogy: Restaurant Kitchen
# Multithreading --> One chef with multiple hands (threads) working on different tasks—but they all share the same brain (memory).
# Good for tasks like chopping veggies while waiting for water to boil.
# Multiprocessing --> Multiple chefs (processes), each with their own brain and station. They work independently and truly in parallel
# great for cooking multiple complex dishes at once.

# Core Differences --->
# Feature	            Multithreading	                            Multiprocessing
# ----------------------------------------------------------------------------------------------------
# Execution Model	    Multiple threads in one process	            Multiple independent processes
# Memory	            Shared memory space	                        Separate memory space
# Parallelism	        Limited by GIL (Global Interpreter Lock)	True parallelism across CPU cores
# Best For	            I/O-bound tasks (file, network, sleep)	    CPU-bound tasks (math, image processing)
# Setup Complexity	    Easier to implement	                        Slightly more complex (IPC, serialization)
# Performance	        Faster for I/O-heavy workloads	            Faster for CPU-heavy workloads

# Example Use Cases --->

# Multithreading:
# Web scraping multiple pages
# Reading/writing files concurrently
# Keeping a GUI responsive

# Multiprocessing:
# Image or video processing
# Data science computations
# Machine learning model training

import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

if __name__ == "__main__":
    # Create two processes
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Both processes completed!")
