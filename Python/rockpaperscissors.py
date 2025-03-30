import random

choices = ['rock', 'paper', 'scissors']

# randomly select a choice for the computer
computer_choice = random.choice(choices)

# ask player for input
print("Let's play rock, paper, scissors")
player_choice = input("Make a choice(either rock, paper, scissors): ")

# print the computer's choice
print(f"Computer chose: {computer_choice}")

# initializing a winner variable
winner=""

# check if the player's choice beats the computer's choice
if (player_choice=="rock" and computer_choice=="scissors") or (player_choice=="scissors" and computer_choice=="paper") or (player_choice=="paper" and computer_choice=="rock"):
    winner = "Player"
    print("You won")
elif player_choice == computer_choice:
    winner = "Tie"
    print("It's a tie")
else:
    winner = "Computer"
    print("Computer won")

