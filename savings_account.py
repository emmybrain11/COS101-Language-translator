from Account import Account
class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02  # Example interest rate
        self.withdraw_limit = 100  # Assignment Requirement 1: Add withdraw limit

    # Assignment Requirement 2: Override the withdrawal behavior
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal denied. Requested amount ({amount}) exceeds the withdrawal limit of {self.withdraw_limit}.")
        else:
            super().withdraw(amount)

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")

print("---Savings Account---")
savings = Savings("Alice", 1000)
print(f"Initial balance: {savings.get_balance()}")

savings.deposit(500)

print("\n---Attempting to withdraw 200---")
savings.withdraw(200)

print("\n---Attempting to withdraw 50---")
savings.withdraw(50)

print("\n---Applying Interest---")
savings.apply_interest()