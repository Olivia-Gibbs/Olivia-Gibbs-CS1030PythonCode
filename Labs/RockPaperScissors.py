# Rock Paper Scissors 
# Rules: rock blunts scissors, paper covers rock, scissors cut paper
# Letters: r=rock, p= paper, s= scissors

import random 

CHOICES= ("r", "p", "s")
NAMES= {"r": "rock", "p": "paper", "s": "scissors"}
BEATS= {"r": "s", "p": "r", "s": "p"}

# Function for player choice 
def get_player_choice():
    """ Ask until player types r, p or s. Returns that letter (lowercase)"""
    choice= ""
    while choice not in CHOICES: 
        choice= input("rock (r), paper (p) or scissors (s)?").strip().lower()
        if choice not in CHOICES: 
            print("Invalid choice. Please type r, p or s.")
    return choice


# Function for Number to Letter
def number_to_letter(number):
    """Convert 1, 2, or 3 to 'r', 'p', 's'."""
    if number== 1:
        letter= "r"
    elif number == 2:
        letter="p"
    else:
        letter= "s"
    return letter 

# Function Computer Choice
def computer_choice():
    """Pick a random number from 1 to 3 and return the matching letter."""
    number = random.randint(1, 3)
    return number_to_letter(number)
    