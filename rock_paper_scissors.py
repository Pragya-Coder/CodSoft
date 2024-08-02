import random

def user_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in choices:
        print("Invalid choice. Please choose from rock, paper, scissors.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def who_is_winner(choice, _choice):
    if choice == _choice:
        return "It is a tie!"
    elif (choice == 'rock' and _choice == 'scissors') or \
        (choice == 'paper' and _choice == 'rock') or \
        (choice == 'scissors' and _choice == 'paper'):
        return "You Win!"
    else:
        return "You lose!"
    
def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    choice = user_choice()
    _choice = computer_choice()
    print(f"You chose: {choice}")
    print(f"Computer chose: {_choice}")

    result = who_is_winner(choice, _choice)

    print(result)

if __name__ == "__main__":
    play_game()