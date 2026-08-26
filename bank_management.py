# Bank Management System - Python Project
# Created by: Kashish

class BankAccount:
    def _init_(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} Deposited. New Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Rs.{amount} Withdrawn. New Balance: Rs.{self.balance}")

    def display(self):
        print(f"\n--- Account Details ---")
        print(f"Account No: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: Rs.{self.balance}")

# Main System
accounts = {}

while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = int(input("Enter Initial Balance: "))
        accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account Created Successfully!")

    elif choice == '2':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[acc_no].deposit(amt)
        else:
            print("Account Not Found!")

    elif choice == '3':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amt = int(input("Enter Amount to Withdraw: "))
            accounts[acc_no].withdraw(amt)
        else:
            print("Account Not Found!")

    elif choice == '4':
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            accounts[acc_no].display()
        else:
            print("Account Not Found!")

    elif choice == '5':
        if not accounts:
            print("No Accounts Found!")
        else:
            for acc in accounts.values():
                acc.display()

    elif choice == '6':
        print("Thank you for using Bank Management System!")
        break
    else:
        print("Invalid Choice!")
