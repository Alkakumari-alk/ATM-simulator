# Account Data
account_number = "568976578"
pin = "1234"
balance = 50000.0
transaction_history = []  # Stores mini statement entries

#********basic display function*******

def display_welcome():
    print("\n" + "="*40)
    print("       WELCOME TO PYTHON ATM")
    print("="*40)
 
 
def display_menu():
    print("\n-------- MAIN MENU --------")
    print("  1. Check Balance")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. Mini Statement")
    print("  5. Exit")
    print("---------------------------")
 
 
def add_transaction(transaction_type, amount):
    """Adds a record to transaction history."""
    entry = f"{transaction_type:<12} | Rs. {amount:>10.2f} | Balance: Rs. {balance:.2f}"
    transaction_history.append(entry)

#  PIN SECURITY
def verify_pin():
    """Verifies PIN with max 3 attempts. Returns True if correct."""
    global pin
    attempts = 3
 
    while attempts > 0:
        entered_pin = input("\nEnter your 4-digit PIN: ").strip()
 
        if entered_pin == pin:
            print(" PIN verified successfully!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f" Incorrect PIN! {attempts} attempt(s) remaining.")
            else:
                print(" Card blocked! Too many incorrect attempts.")
                return False
 
    return False
#ATM OPERATIONS
 
def check_balance():
    """Displays current account balance."""
    print("\n------- ACCOUNT BALANCE -------")
    print(f"  Account No : {account_number}")
    print(f"  Balance    : Rs. {balance:.2f}")
    print("--------------------------------")
 
 
def deposit():
    """Handles money deposit."""
    global balance
 
    print("\n--------- DEPOSIT ---------")
 
    try:
        amount = float(input("Enter deposit amount: Rs. "))
    except ValueError:
        print(" Invalid amount! Please enter a number.")
        return
 
    if amount <= 0:
        print(" Amount must be greater than 0.")
        return
 
    if amount > 100000:
        print(" Single deposit limit is Rs. 1,00,000.")
        return
 
    balance += amount
    add_transaction("DEPOSIT", amount)
    print(f" Rs. {amount:.2f} deposited successfully!")
    print(f"   Updated Balance: Rs. {balance:.2f}")
 
 
def withdraw():
    """Handles money withdrawal."""
    global balance
 
    print("\n-------- WITHDRAWAL --------")
 
    try:
        amount = float(input("Enter withdrawal amount: Rs. "))
    except ValueError:
        print(" Invalid amount! Please enter a number.")
        return
 
    if amount <= 0:
        print(" Amount must be greater than 0.")
        return
 
    if amount % 100 != 0:
        print(" Amount must be in multiples of Rs. 100.")
        return
 
    if amount > 20000:
        print(" Single withdrawal limit is Rs. 20,000.")
        return
 
    if amount > balance:
        print(" Insufficient balance!")
        print(f"   Available Balance: Rs. {balance:.2f}")
        return
 
    balance -= amount
    add_transaction("WITHDRAWAL", amount)
    print(f" Rs. {amount:.2f} dispensed. Please collect your cash.")
    print(f"   Remaining Balance: Rs. {balance:.2f}")
 
 
def mini_statement():
    """Displays last 5 transactions."""
    print("\n------- MINI STATEMENT -------")
    print(f"  Account No: {account_number}")
    print("-" * 50)
 
    if not transaction_history:
        print("  No transactions found.")
    else:
        # Show last 5 transactions
        recent = transaction_history[-5:]
        print(f"  {'TYPE':<12} | {'AMOUNT':>13} | {'BALANCE'}")
        print("-" * 50)
        for record in recent:
            print(f"  {record}")
 
    print("-" * 50)
    print(f"  Current Balance: Rs. {balance:.2f}")
    print("-------------------------------")
#MAIN PROG.
 
def main():
    display_welcome()
    print(f"\n  Account No: {account_number}")
 
    # Step 1: PIN Verification
    if not verify_pin():
        print("\nExiting... Thank you!")
        return
 
    # Step 2: Main Menu Loop
    while True:
        display_menu()
 
        choice = input("Enter your choice (1-5): ").strip()
 
        if choice == "1":
            check_balance()
 
        elif choice == "2":
            deposit()
 
        elif choice == "3":
            withdraw()
 
        elif choice == "4":
            mini_statement()
 
        elif choice == "5":
            print("\n Thank you for using Python ATM!")
            print("   Please collect your card. Goodbye!\n")
            break
 
        else:
            print(" Invalid choice! Please enter a number between 1 and 6.")
 
        # Ask if user wants to continue
        cont = input("\nGo back to main menu? (y/n): ").strip().lower()
        if cont != "y":
            print("\nThank you for using Python ATM! Goodbye!\n")
            break
 
 
# Run the program
if __name__=="__main__":
    main()