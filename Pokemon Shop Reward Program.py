# Pokemon Shop Reward Program

import random
import time

# Chance to win
def chanceToWin():
    
    # Odds of winning each prizes
    prize = {
        #"Mew EX SIR": 2000,
        #"Mew Metal Card": 1500,
        #"Mewtwo IR": 1000,
        "Full Art": 500,
        "Full Art V": 250,
        "Mini Tin": 200,
        "Energy Pack": 100,
        "EX Card": 50,
        "Poster Collection": 25,
        "Holo": 10,
        "Reverse Holo": 5
        }

    # Checking to see if prize is won
    for key in prize:
        userNumber = random.randint(1, prize[key])          # Selecting user's number
        winningNumber = random.randint(1, prize[key])      # Selecting winning number

        # Has the user won?
        win = False
        
        # Let user know what they won
        if userNumber == winningNumber:
            gameResultAnnoucement()
            print("********************")
            print("**                             **")
            print("**     YOU WIN A(N)     **")
            print("**                             **")
            print("********************")
            time.sleep(1.5)
            print("--------------------------")
            print(key.upper())
            print("--------------------------")
            win = True
            break
            
    # Let user know they did not win
    if(win == False):
            gameResultAnnoucement()
            print("Sorry, you did not win this time.")

    goAgain = input("Press Enter to go again: ")
    if(goAgain == ""):
        chanceToWin()
    else:
        print("See you next time!")

def gameResultAnnoucement():

    # Anticipation text before result is shown
    print("Shuffling...........")
    time.sleep(0.2)
    print("Shuffling.............")
    time.sleep(0.1)
    print("Drawing..........")
    time.sleep(0.3)
    print("--------------------------")
    time.sleep(0.5)
    print("            RESULT IS           ")
    time.sleep(0.5)
    print("--------------------------")
    time.sleep(0.5)
            
# Start of program
def main():

    chanceToWin()

    
# Start of the program
main()
