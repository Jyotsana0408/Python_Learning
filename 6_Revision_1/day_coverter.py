seconds  = int(input("Enter second: "))

days = seconds//86400

remaining = seconds % 86400

hours = remaining // 3600

remaining = seconds % 3600

min = remaining // 60

print(f"{days:02}:{hours:02}:{min:02}")