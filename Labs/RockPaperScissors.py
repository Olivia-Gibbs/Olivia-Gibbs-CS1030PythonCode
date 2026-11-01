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
def get_computer_choice():
    """Pick a random number from 1 to 3 and return the matching letter."""
    number = random.randint(1, 3)
    return number_to_letter(number)

# Determine Winner Function 
def determine_winnner(player, computer):
    """Return 'tie', 'win' (player wins) or 'lose' (computer wins)."""
    if player== computer: 
        result= "tie"
    elif BEATS [player] ==computer: #player's choice beats computer's 
        result= "win"
    else: 
        result="lose"
    return result 

# Function for the result message 
def result_message(result):
    """ Turn a result wrod into the text shown to the player."""
    if result == "tie":
        message= "DRAW!"
    elif result=="win":
        message= "YOU WIN!"
    else:
        message= "COMPUTER WINS!"
        return message 

    #Function Scoreboard 
    def new_scoreboard(): 
        return {"win": 0, "tie": 0, "lose": 0}

    #Function Update Score 
    def update_score(score,result): 
        """Add one to the win/ tie/lose count."""
        score[result]= score[result]+ 1
        return score

    # Function Percentage 
    def win_percentage(score):
        """Percent of games the player won (0.0 if no games yet)."""
        total= score ["win"] + score["tie"] + score ["lose"]
        if total== 0:
            return 0.0
        return score ["win"]/total *100

    # Function for displaying the score 
    def display_score(score):
        print(f"Score -> Wins: {score['win']} Ties: {score['tie']}"
              f"Losses: {score['lose']} (Win rate: {win_percentage(score):.Of}%")

        #Function for Asking for Playing Again 
        def ask_play_again():
            """Return True only when the player enters y. Anything else exists."""
            answer= input("Do you want to play again? Enter y:"). strip().lower()
            return answer== "y"

        # Function for scoring rounds
        def play_round(score):
            """Play one game, show the outcomes, update and show the score."""
            player= get_player_choice()
            computer= get_computer_choice()
            print(f"{NAMES[player]} ({player} vs {NAMES[computer]} ({computer})")
            result= determine_winnner(player,computer)
            print(result_message(result))
            update_score(score,result)
            display_score(score)

            def main ():
                score= new_scoreboard()
                play_again= True 
                while play_again:
                    play_round(score)
                    play_again= ask_play_again()
                    print("Thanks for playing!")
            if __name__ == "__main__":
                   main()
             