from ascii_art import *

print(treasure)
print("Welcome to Treasure Island.\nYour mission is to find the treasure. \n")

# using .lower() to make the input uniform

choice = (input("Do you want to go left or right? ")).lower()

if choice == 'left' :
    print(island)
    choice2 = (input("Do you want to swim or wait? ")).lower()

    if choice2 == 'wait' :
        print(doors)
        choice3 = (input('Enter the color of door you want to enter : \n')).lower()
        if choice3 == 'yellow':
            print(win)
            print('You Win!')

        elif choice3 == 'red' :
            print(fire_game_over)
            print('You are burned by fire.  Game Over!')

        elif choice3 == 'blue' :
            print('You are eaten by beasts. Game Over!')

    else:
        print('You were attacked by a Trout. Game Over!')

else:
    print('You fell into the hole. Game Over!')
