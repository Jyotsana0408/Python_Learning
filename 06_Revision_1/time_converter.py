seconds  = int(input("Enter second: "))

hours = seconds//3600

remaining_sec = seconds - (hours* 3600)

min = remaining_sec//60

seconds = remaining_sec - (min * 60)

print(f"{hours:02}:{min:02}:{seconds:02}")