import random
from rpsasci import *


choose = [rock,paper,scissors]
print("What do you choose? ")
userChoice = int(input("Type 0 for Rock, 1 for Paper or 2 for scissors. "))
print("You chose ")
print(choose[userChoice])
print("Computer chose ")
pcChoice = random.randint(0, 2)
print(choose[pcChoice])
if userChoice == 0 and pcChoice == 1:
    print("You lose. ")
elif userChoice == 0 and pcChoice == 2:
    print("You win. ")
elif userChoice == 1 and pcChoice == 0:
    print("You win. ")
elif userChoice == 1 and pcChoice == 2:
    print("You lose. ")
elif userChoice == 2 and pcChoice == 1:
    print("You win. ")
elif userChoice == 2 and pcChoice == 0:
    print("You lose")
elif userChoice == pcChoice:
    print("It is a draw. ")
else:
    print("invalid choice")