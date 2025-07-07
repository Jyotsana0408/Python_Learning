# asyncio is Python’s built-in library for asynchronous programming, 
# designed to help you write code that can do multiple things at once—without using threads or processes.

# What Is Asynchronous Programming?
# It’s a way to run tasks concurrently, especially useful when your program spends time waiting—like 
# for network responses, file I/O, or user input.
# Instead of blocking the program while waiting, asyncio lets other tasks run in the meantime.

# Core Concepts --->
# Concept	                Description
# -------------------------------------------
# async def	                Defines a coroutine (an async function)
# await	                    Pauses the coroutine until the awaited task finishes
# asyncio.run()	            Starts the event loop and runs the coroutine
# asyncio.create_task()	    Schedules a coroutine to run concurrently

# When to Use asyncio --->
# Making API calls or web requests
# Reading/writing files or databases
# Building chatbots, servers, or CLI tools that wait for input
# Handling multiple tasks without blocking

import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("This is function1")
    return "func1"

async def function2():
    await asyncio.sleep(1)
    print("This is function2")
    

async def function3():
    await asyncio.sleep(3)
    print("This is function3")
   

# async def main():
#     task = asyncio.create_task(function1())
#     # function1()
#     await function2()
#     await function3()

async def main():
    L = await asyncio.gather(
         function1(),
         function2(),
         function3()
    )

    print(L)
asyncio.run(main())
