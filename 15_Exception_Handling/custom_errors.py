# raise custom errors

a = int(input("enter any value between 4 to 9: "))
if (a<4) or (a>9):
    raise ValueError("Value should be 4 and 9")

