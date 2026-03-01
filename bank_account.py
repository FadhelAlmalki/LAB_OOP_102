class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        if not account_holder or not isinstance(account_holder, str):
            raise ValueError("Account holder name must be a non-empty string.")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")

        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance

    def get_account_holder(self) -> str:
        return self.account_holder

