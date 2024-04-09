import random

options = ["rock", "paper", "scissor"]

while True:
    try:
        playerchoice = input("Choose one: rock, paper, or scissors: ").lower()
        
        if playerchoice == "finish game":
            raise Exception("Game finished")
        
        while playerchoice not in options:
            print("Not an option")
            playerchoice = input("Choose one: rock, paper, or scissors: ").lower()

        computerchoice = random.choice(options)

        print("Player:", playerchoice)
        print("Computer:", computerchoice)

        if playerchoice == computerchoice:
            print("Tie")
        elif (playerchoice == "rock" and computerchoice == "scissor") or (playerchoice == "paper" and computerchoice == "rock") or (playerchoice == "scissor" and computerchoice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

    except Exception as a:
        print("Game was stopped by user:", a)
        break