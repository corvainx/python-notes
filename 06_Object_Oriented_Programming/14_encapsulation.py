# Lesson 14: Encapsulation and Access Modifiers
# - Public (name): Accessible anywhere.
# - Protected (_name): Hint that attribute is internal to class/subclass.
# - Private (__name): Name-mangled to prevent direct external access.

class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner          # Public
        self._account_type = "Checking" # Protected
        self.__balance = initial_balance # Private

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New Balance: ${self.__balance:.2f}")
        else:
            print("Transaction Rejected: Insufficient funds or invalid amount.")

    def get_balance(self) -> float:
        return self.__balance

account = BankAccount("Dexter", 1000.0)
account.deposit(250.0)
account.withdraw(500.0)
print(f"Verified Balance: ${account.get_balance():.2f}")
