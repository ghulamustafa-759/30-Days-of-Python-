import random as r


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

cardHuman = []
card_comp = []


def initial():
    #first 2 random card picks
    for i in range(0,2):
        card_pick = cards[r.randint(2,11)]
        card_pick2 = cards[r.randint(2,11)]
        cardHuman.append(card_pick)
        card_comp.append(card_pick2)
    humancards = cardHuman
    card_score = sum(humancards)
    print(f"Your cards : {humancards}, current score : {card_score}")
    comp_card1 = card_comp[0] 
    print(f"Computer's first card is : {comp_card1} ")

def another():
    card_pick = cards[r.randint(2,11)]
    cardHuman.append(card_pick)
    sumcardhuman = sum(cardHuman)
    sumcardcomp = sum(card_comp)

    if sumcardhuman > 21 or sum(cardHuman) > sum(card_comp):
        print(f"You loose! \nyour sum is {sumcardhuman} .")
        print(f"final hand is {cardHuman}, current score : {sum(cardHuman)}, \n computers final hand is {card_comp}, computer's score is {sum(card_comp)}")
    else:
        print(f"You Win! \nfinal hand is {cardHuman}, current score : {sum(cardHuman)}, \ncomputers final hand is {card_comp}, computer's score is {sum(card_comp)}")
def pas():
    if sum(cardHuman) < 21 and sum(cardHuman) > sum(card_comp):
        print(f"You win! \nfinal hand is {cardHuman}, current score : {sum(cardHuman)}, \ncomputers final hand is {card_comp}, computer's score is {sum(card_comp)}")
    else:
        print(f"You lose! \nfinal hand is {cardHuman}, current score : {sum(cardHuman)}, \ncomputers final hand is {card_comp}, computer's score is {sum(card_comp)}")
play_again = True


initial()
decision = input("Type 'y' to get another card, type 'n' to pass : ").lower()
if decision == 'y':
    another()
else:
    pas()
    

