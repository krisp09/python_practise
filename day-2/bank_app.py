from bank_account import BankAccount, InsufficientFundsError

def main():
    account = BankAccount(account_number="123456789", balance=1000)
    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            try:
                new_balance = account.deposit(amount)
                print(f"Deposited ${amount:.2f}. New balance: ${new_balance:.2f}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            try:
                new_balance = account.withdraw(amount)
                print(f"Withdrew ${amount:.2f}. New balance: ${new_balance:.2f}")
            except ValueError as e:
                print(e)
            except InsufficientFundsError as e:
                print(e)

        elif choice == '3':
            account.get_balance()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()