import random

print("Welcome to the Number Guessing Game ! \nI'm thinking of a number between 1 and 100 ")



NUM = random.randint(1, 100)

def easy():
    for attempts in range(10,0,-1):
            print(f"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess : "))
            if guess == NUM:
                print("This is the number, you won!")
                break
            else:
                if NUM > guess:
                     print("Too Low!")
                else:
                     print("Too High!")

def hard():
     for attempts in range(5,0,-1):
            print(f"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess : "))
            if guess == NUM:
                print("This is the number, you won!")
                break
            else:
                if NUM > guess:
                     print("Too Low!")
                else:
                     print("Too High!")

mode = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

if mode == 'easy':
     easy()
elif mode == 'hard':
     hard()
else:
     print("Invalid Mode!")