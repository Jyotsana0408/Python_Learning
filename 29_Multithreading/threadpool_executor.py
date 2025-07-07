# concurrent.futures --->
# high-level Python module that helps you run tasks in parallel—either using threads or processes
# without diving deep into low-level concurrency code.

# Why Use It? --->
# It simplifies running multiple functions at the same time, especially when:
# You want to speed up I/O-bound tasks (like downloading files or reading data).
# You need to parallelize CPU-heavy tasks (like image processing or calculations).

# Key Components--->
# Class	                Best For	        Description
# ThreadPoolExecutor	I/O-bound tasks	    Uses threads to run tasks concurrently
# ProcessPoolExecutor	CPU-bound tasks	    Uses separate processes for true parallelism


import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)


def main():
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

def poolingDemo():
    # submit() schedules a function to run.
    # future.result() waits for the result.

    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # print(future1.result())

        # future2 = executor.submit(func, 2)
        # print(future2.result())

        # future3 = executor.submit(func, 4)
        # print(future3.result())

        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())

poolingDemo()


