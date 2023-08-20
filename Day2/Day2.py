print("Welcome to Tip Calculator")

bill = int(input("Enter the total amount of the bill : "))
guests = int(input("Enter the number of people who will split the bill : "))

tip = int(input("Enter the percentage you want to tip : "))

# as tip is in percentage, to calculate actual tip amount, we use this formula

tip_amount = (tip/100)*bill

total_bill = bill + tip_amount


print(f"Your total bill is {total_bill} .")

# fstring is being used,it is a method in python, for using objects in strings

# now to split the bill equally

per_head = total_bill/guests

print(f"The bill for each person is {per_head} .")
