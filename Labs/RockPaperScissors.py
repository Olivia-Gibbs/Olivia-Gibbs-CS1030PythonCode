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
    """Convert 1, 2, or 3 to the corresponding choice letter."""
    return CHOICES[number - 1]