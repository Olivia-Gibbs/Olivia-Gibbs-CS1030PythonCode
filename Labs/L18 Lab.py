# These are the test cases 

#C1 Card Valid 
# 1 False 
#2 False 
#3 False
#4 True 
#5 True 

#C2 Pin Correct 
#1 False 
#2 True 
#3 False 
#4 Ture 

#C3
#1 Invalid acess card
#2 Invalid acess card 
#3 Acess card acepted then Incorrect PIN 
#4 Acess card acepted then Acess Granted 

#4 Purpose 
#1 Bad card, so the pin in never checked
#2 A correct PIN must not rescue a bad card 
#3 Card passess, PIN fails 
#4 Everything passes 

#Other notes 
# Row two is most important it proves the card is chekced before the pin 

#This is the Pseudcode (reminder this is English plus strucutre not Python syntx!)

#SET card_valid to true or false 
#SET pin_correct to true or false 

#IF card_valid is ture 
# DISPLAY "Acess card acepted"
#IF pin_correct is true 
#DISPLAY "Acess granted"

#ELSE 
#DISPLAY "Incorrect PIN"
#ELSE 
#Display "Invalid acess card"

#Other Notes 
#THe PIN check sits inside the card-valid branch. THat nesting is what makes the PIN check depend on the card

#The Code Itself 

#Secure Building Acess 
#Chcks the acess card first, then the PIN (only if the card is valid)

card_valid= True 
# Make sure to change the values to test each combination 
# This is Boolean variable. It holds only Ture or Fals, with capital letter first and no quotes. In quotes would make a stirng 
pin_correct= False 

if card_valid:
    print("Access card accepted")
    if pin_correct:
        print("Access Granted")
    else:
        print("Incorrect PIN")
else:
    print("Invalid access card")

