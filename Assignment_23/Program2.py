# 2. Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (__init__) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display() – displays account holder name and current balance.
# Deposit() – accepts an amount from the user and adds it to the balance.
# Withdraw() – accepts an amount from the user and subtracts it from the balance
# (ensure withdrawal is allowed only if sufficient balance exists).
# CalculateInterest() – calculates and returns interest using the formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects of the BankAccount class and demonstrate all methods.


class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.name = input("Enter Account Holder Name: ")
        self.amount = int(input("Enter Amount: "))

    def Display(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Amount: {self.amount}")

    def Deposit(self):
        deposit_amount = int(input("Enter Deposit Amount: "))
        self.amount += deposit_amount
        print(f"Amount after deposit: {self.amount}")

    def Withdraw(self):
        withdraw_amount = int(input("Enter Withdraw Amount: "))
        if withdraw_amount > self.amount:
            print("Insufficient balance")
        else:
            self.amount -= withdraw_amount
            print(f"Amount after withdrawal: {self.amount}")

    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print(f"Interest: {interest}")

def main():
    account1 = BankAccount()
    account1.Display()
    account1.Deposit()
    account1.Withdraw()
    account1.CalculateInterest()

    account2 = BankAccount()
    account2.Display()
    account2.Deposit()
    account2.Withdraw()
    account2.CalculateInterest()

if __name__ == "__main__":
    main()