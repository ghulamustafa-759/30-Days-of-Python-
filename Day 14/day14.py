from art_d14 import logo,vs
from game_data_d14 import data
import random


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    
    return(f"{account_name}, a {account_descr}, from {account_country}")

print(logo)
score = 0
game_should_continue = True
while game_should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)} .\n")
    print(f"{vs}\n")
    print(f"Against B : {format_data(account_b)} .")

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    def check_answer(guess, a_follower_count, b_follower_count):
        if a_follower_count > b_follower_count:
            return guess == "a"
        else:
            return guess == "b"

    is_correct = check_answer(guess, a_follower_count, b_follower_count)



    if is_correct:
        score+=1
        print(f"You are right! Current Score is : {score}")
        game_should_continue = True

        
    else:
        print(f"You are wrong! Final Score is : {score}")
        game_should_continue = False


