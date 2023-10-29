# Pokemon Shop Reward Program

import random

# Chance to win
def chanceToWin(oddsOfWinning):

    userNumber = random.randint(1, oddsOfWinning)
    winningNumber = random.randint(1, oddsOfWinning)

    if userNumber == winningNumber:
        print("you win")
    else:
        print("You lose")

# Chance to win Mew EX SIR
def oddsOfPrizes():

    prize = {
        2000: "Mew EX SIR",
        #"Mew Metal Card": 1500,
        1000: "Mewtwo IR"
        #"Full Art": 500,
        #"Full Art V": 250,
        #"Half ex": 50,
        #"Holo": 10,
        #"Reverse Holo": 5
        }

    n = 01
    for key in prize:
        print(userNumber = random.randint(1, prize))
        print(winningNumber = random.randint(1, prize))
                             
                             
    

# Start of program
def main():

    oddsOfPrizes()

    
# Start of the program
main()
