import random

def get_user_choice():
    """Get user's choice."""
    print("Enter your choice: rock, scissors, or paper.")
    user_choice = input().lower()
    while user_choice not in ["rock", "scissors", "paper"]:
        print("That's not a valid choice. Please enter rock, scissors, or paper.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    """Get computer's choice."""
    return random.choice(["rock", "scissors", "paper"])

def determine_winner(user, computer):
    """Determine the winner."""
    if user == computer:
        return "It's a tie!"
    if (
        (user == "rock" and computer == "scissors")
        or (user == "scissors" and computer == "paper")
        or (user == "paper" and computer == "rock")
    ):
        return "Congratulations! You win!"
    else:
        return "Oops! The computer wins. Try again?"

def play_game():
    """Play the game."""
    print("Welcome to Rock, Scissors, Paper!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

# Run the game
play_game()
