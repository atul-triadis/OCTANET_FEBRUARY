class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate(self, pin_attempt):
        return self.pin == pin_attempt

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
            print(f"Withdrawn ${amount}. Remaining balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Transfer to {recipient}: ${amount}")
            print(f"Transferred ${amount} to {recipient}. Remaining balance: ${self.balance}")

    def __str__(self):
        return f"User ID: {self.user_id}, Balance: ${self.balance}"

class ATM:
    def __init__(self):
        self.users = {}

    def display_menu(self):
        print("ATM Menu:")
        print("1. View Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def create_account(self):
        user_id = input("Enter your new User ID: ")
        pin = input("Create a PIN: ")
        self.users[user_id] = User(user_id, pin)
        print("Account created successfully.")

    def login(self):
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")
        user = self.users.get(user_id)
        if user and user.authenticate(pin):
            print("Login successful.")
            return user
        else:
            print("Invalid User ID or PIN.")
            return None

    def handle_transaction(self, user):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                user.view_transaction_history()
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)
            elif choice == "4":
                amount = float(input("Enter amount to transfer: "))
                recipient = input("Enter recipient's name: ")
                user.transfer(amount, recipient)
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    atm = ATM()

    while True:
        print("Welcome to the ATM.")
        print("1. Login")
        print("2. Create a new account")
        print("3. Quit")
        option = input("Choose an option: ")

        if option == "1":
            user = atm.login()
            if user:
                atm.handle_transaction(user)
        elif option == "2":
            atm.create_account()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
