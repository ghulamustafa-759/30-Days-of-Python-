#requirements
    #print report
    #check resources suficent
    #process coins
    #check transaction successful

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#resource check
def resource():
    print (f"\nWater : {resources['water']}\nMilk : {resources['milk']}\nCoffee : {resources['coffee']}")

#take order
order = input("What would you like? (espresso/latte/cappucino): ").lower()
if order == 'report':
    resource()
print("Please insert coins. \n")
coin_quarter = input("How many quarters? : ")
coin_dimes = input("How many dimes? : ")
coin_nickles = input("How many nickles? : ")
coin_pennies = input("How many pennies? : ")

penny = 0.01*float(coin_pennies)
nickles = 0.05*float(coin_nickles)
dimes = 0.1*float(coin_dimes)
quarter = 0.25*float(coin_quarter)

total_dollars = round(penny+nickles+dimes+quarter,2)
print(total_dollars)
if order == "espresso":
    if total_dollars > float(MENU["espresso"]["cost"]):
        change = total_dollars-float((MENU["espresso"]["cost"]))
        print(f"Here is ${change} in change.")
        resources["coffee"] -= (MENU["espresso"]["ingredients"]["coffee"])
        resources["water"] -= (MENU["espresso"]["ingredients"]["water"])
    else:
        print("Sorry that is not enough money. Money refunded.")

#elif order == "cappucino":
if order == "cappucino":
    if total_dollars > float(MENU["cappucino"]["cost"]):
        change = total_dollars-float((MENU["cappucino"]["cost"]))
        print(f"Here is ${change} in change.")
        resources["coffee"] -= (MENU["cappucino"]["ingredients"]["coffee"])
        resources["milk"] -= (MENU["cappucino"]["ingredients"]["milk"])
        resources["water"] -= (MENU["cappucino"]["ingredients"]["water"])
        
    else:
        print("Sorry that is not enough money. Money refunded.")


if order == "latte":
    if total_dollars > float(MENU["espresso"]["cost"]):
        change = total_dollars-float((MENU["espresso"]["cost"]))
        print(f"Here is ${change} in change.")
        resources["coffee"] -= (MENU["latte"]["ingredients"]["coffee"])
        resources["milk"] -= (MENU["latte"]["ingredients"]["milk"])
        resources["water"] -= (MENU["latte"]["ingredients"]["water"])
    else:
        print("Sorry that is not enough money. Money refunded.")
#coins insert, count, change

