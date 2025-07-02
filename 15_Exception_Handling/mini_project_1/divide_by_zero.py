x = int(input("Enter an integer: "))

try:
    result = x / 0  # This will raise ZeroDivisionError
    print("Divisible result is:", result)
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)