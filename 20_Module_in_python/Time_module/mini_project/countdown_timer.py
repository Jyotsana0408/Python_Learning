import time

def countdown(seconds):
    print(f"Countdown starts for {seconds} seconds...")
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Get user input
user_input = int(input("Enter countdown time in seconds: "))
countdown(user_input)
