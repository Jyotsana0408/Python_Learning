num = int(input("Enter a number: "))
fact =  1

if num <0:
    print("enter positive number")
elif num == 0:
    print("number can't be zero")
else:
    for i in range(1, num+1):
        fact *= i
    print(fact)