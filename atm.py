import time

account_funds = 0
statement = []

def options():
    option = int(input("""
    Enter 1 to view balance
    Enter 2 to deposit
    Enter 3 to withdraw
    Enter 4 to view previous transactions\n"""))
    return option

def deposit():
    global account_funds, statement
    try:
        deposit_amount = float(input("How much would you like to deposit?\n"))
        if deposit_amount > 0:
            account_funds += deposit_amount
            print(f"Success: you have deposited £{deposit_amount:.2f}. Your new balance is £{account_funds:.2f}.")
            t = time.time()
            log_statement(t, deposit_amount)
        else:
            print("Please make sure you deposit an amount greater than 0.")
    except ValueError:
        print("Oops that didn't work. Please make sure you enter a number.")
    
def log_statement(t, deposit_amount):
    global account_funds, statement
    statement.append((t, deposit_amount, account_funds))

def display_statement():
    global statement
    if len(statement) == 0:
        print("There has been no activity on this account as of yet.")
    else:
        for item in statement:
            t,deposit_amount, account_funds = item
            print(f"Date:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}, Transaction:{deposit_amount:.2f}, Balance:{account_funds:.2f}")

def show_balance():
    global account_funds
    print(f'Your current balance is £{account_funds:.2f}')

def withdraw():
    global account_funds, statement
    try:
        withdraw_amount = float(input("How much would you like to withdraw?\n"))
        if withdraw_amount > account_funds:
            print(f"Sorry this transaction could not be completed as you only have £{account_funds:.2f} available to withdraw.")
        elif withdraw_amount<1:
            print("Sorry the minimum amount you can withhdraw is £1.")
        else:
            account_funds -= withdraw_amount
            print(f"Success: you have withdrawn £{withdraw_amount:.2f}. Your new balance is £{account_funds:.2f}.")
            t = time.time()
            log_statement(t, -withdraw_amount)
    except ValueError:
        print("Oops that didn't work. Please make sure you enter a number.")

    
def return_to_options():
    go_again = input("Enter 'Y' if you'd like to return to the main menu (OR any other key to exit)\n")
    if len(go_again)>=1 and go_again[0].lower() == 'y':
        return True
    
    return False

def main():
    global account_funds, statement
    print("Welcome to the Bank App")
    while True:
        option = options()
        if option == 1:
            show_balance()
            if not return_to_options():
                break            
        elif option == 2:
            deposit()
            if not return_to_options():
                break    
        elif option == 3:
            withdraw()
            if not return_to_options():
                break    
        elif option == 4:
            display_statement()
            if not return_to_options():
                break    
        else:
            print("Sorry, that is not a valid option. Please try again.")
    print("Thanks for using our ATM. Bye!")

main()
