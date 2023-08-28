

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):    
    return num1 - num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2
def mod(num1, num2):
    return num1%num2

def calculator():
    num_a = float(input("Enter the first number : \n"))


    operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div,
        "%": mod
        }
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_selected = input("Enter the operation you want to perfrom : ")

        num_b = float(input("Enter the second number : \n"))

        calculation = operations[operation_selected]
        answer = calculation(num_a , num_b)

        print(f"Your ans is {answer}")

        if input(f"Type 'y' to continue calculation with {answer} : type 'n' to start a new calculation : ") == 'y':
            num_a = answer
        else:
            should_continue = False
            calculator()
