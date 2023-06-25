import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ")
    while choice.lower() not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ")
    return choice.lower()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower() == 'yes'

# Main game loop
print("Welcome to Rock-Paper-Scissors!")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    determine_winner(user_choice, computer_choice)

    if not play_again():
        break

print("Thank you for playing!")
