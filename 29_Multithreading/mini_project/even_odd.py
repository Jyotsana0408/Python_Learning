import threading

def print_even():
    for i in range(0, 10, 2):
        print(f"Even: {i} ")

def print_odd():
    for i in range(1, 10, 2):
        print(f"Odd: {i} ")

# Create threads
t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print("Done!")
