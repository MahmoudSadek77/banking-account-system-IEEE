import time

class BankAccount:
    def __init__(self, name, balance, PIN):
        self.name = name
        self.balance = float(balance)
        self.pin = PIN
    def withdraw(self, amount):
       if amount > self.balance:
           print("Not enough credits!")
           time.sleep(2)
           info()
       else:
           self.balance -= amount
           print(f"Successed withdrawn: {amount} $")
           print(f"Your Balance is: {self.balance} $")
           time.sleep(2)
           info()
    def deposit(self, amount):
        if amount < 0:
            print("Invalid Deposit Amount.")
            time.sleep(2)
            info()
        else:
            self.balance += amount
            print(f"Successed Deposited: {amount} $")
            time.sleep(2)
            info()
    def show_Balance(self):
       print(f"Your Balance: {self.balance} $")
       time.sleep(2)
       info()

account = BankAccount("Mahmoud", 5000, 6748)

def info():
    print("Enter your Choice: ")
    print("1: Deposit Money")
    print("2: Withdraw Money")
    print("3: Check Balance")
    print("4: Exit")

def account_login():
    print("#" * 40)
    print("A simple Bank Account System")
    print("#" * 40)
    print("Enter your PIN password: ")
    number_of_attempts = 0
    while True:
        choice = int(input(""))
        if choice == account.pin:
            print("Logged in!")
            print(f"Welcome {account.name}!")
            time.sleep(2)
            return main()
        else:
            number_of_attempts += 1
            print("Invalid PIN")
            print("Try again")
        if number_of_attempts >= 6:
            print("You have ran out of attempts")
            print("Locking down the account")
            exit()

def main():
    print("Enter your Choice: ")
    print("1: Deposit Money")
    print("2: Withdraw Money")
    print("3: Check Balance")
    print("4: Exit")
    while True:
        choice = int(input(""))
        if choice == 1:
            value = float(input("Enter the amount you want to deposit: "))
            account.deposit(value)
        elif choice == 2:
            value = float(input("Enter the amount you want to withdraw: "))
            account.withdraw(value)
        elif choice == 3:
            account.show_Balance()
        elif choice == 4:
            exit()

account_login()
