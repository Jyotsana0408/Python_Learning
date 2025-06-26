import random

guess = random.randint(1,10)
num = int(input("guess the number: "))

if guess == num:
    print("you got it!!")
else:
    print("Oh no , Please guess again.")