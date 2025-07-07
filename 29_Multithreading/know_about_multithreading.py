# Multithreading in Python --->
# lets you run multiple threads (smaller units of a process) at the same time
# great for tasks like file I/O, network requests, or user interactions that don’t need heavy CPU power.

# How to Use It --> import threading

# why Use Multithreading?
# Use Case	            Benefit
# File reading/writing	Avoids blocking the main thread
# Web scraping	        Fetch multiple pages in parallel
# GUI applications	    Keeps UI responsive
# Background tasks	    Run timers, loggers, etc.


# Python’s GIL Limitation
# Python has a Global Interpreter Lock (GIL), which means:
# Threads don’t run in true parallel for CPU-heavy tasks.
# For CPU-bound work, use multiprocessing instead.
# But for I/O-bound tasks, multithreading works beautifully.


import threading
import time

# Without multithreading
# Indicate some task being done
def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    print(f"Finished sleeping for {sec} seconds")

time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()
print(time2-time1)
print("--------------------------------------------------------------------")

# With multithreading

# How It Works
# threading.Thread(...) creates a new thread to run func with its sec argument.
# .start() launches the threads.
# .join() ensures the main program waits until all threads are done.


time3 = time.perf_counter()

# Create thread objects for each sleep duration
t1 = threading.Thread(target=func, args=(4,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))

# start() = “Begin working.”
# join() = “Wait here until you're done.”
# Start all threads
t1.start()
t2.start()
t3.start()
time4 = time.perf_counter()
print(time4-time3)
# Wait for all threads to finish
# Without .join(), your program would keep running and might exit before the threads are done, cutting them off mid-task. 
# Using join() ensures clean execution and that all background tasks get time to finish properly.
t1.join()
t2.join()
t3.join()
# time4 = time.perf_counter()
print(time4-time3)
print("All threads completed!")
