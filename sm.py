MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

def deposite():
    while True:
        amount = input("What would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINE) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please enter a valid line number")
        else:
            print("Please enter a number")

    return lines

def main():
    balance = deposite()
    lines = get_number_of_lines()
    print(balance, lines)

main()