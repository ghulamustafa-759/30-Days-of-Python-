import os

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    print(f"Bidder {bidder} has the highest bid of {highest_bid}")

while not bidding_finished:

    name = input("Enter your name : ")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders?  Type Y/N")
    
    if should_continue.lower() == "n":
        bidding_finished = True
        find_highest_bidder(bids)

    elif should_continue.lower() =="y":
        os.system('cls')
