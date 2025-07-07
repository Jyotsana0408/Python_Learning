import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Battle!")
    rounds = int(input("How many rounds would you like to play? "))
    user_score = 0
    computer_score = 0

    for round_number in range(1, rounds + 1):
        input(f"\nRound {round_number} - Press Enter to roll the dice...")
        user_roll = roll_dice()
        computer_roll = roll_dice()
        
        print(f"You rolled: {user_roll}")
        print(f"Computer rolled: {computer_roll}")

        if user_roll > computer_roll:
            print("You win this round!")
            user_score += 1
        elif user_roll < computer_roll:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

    print("\nFinal Results:")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print("You are the ultimate dice champion!")
    elif user_score < computer_score:
        print("Computer takes the victory!")
    else:
        print("It's a draw. Well played!")

play_game()
