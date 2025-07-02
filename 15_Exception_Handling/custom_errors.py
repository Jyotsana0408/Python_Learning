# raise custom errors

user_input = input("enter any value between 4 to 9 or enter Quit: ")

if user_input.lower() == "quit":
    print("Exiting...")
else:
    a = int(user_input)
    if  (a<4) or (a>9):
        raise ValueError("Value should be between 4 and 9")

