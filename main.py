from bank_account import BankAccount

def main():
    account1 = BankAccount("Fad", 1000)

    print(f"Account Holder: {account1.get_account_holder()}")
    print(f"Initial Balance: ${account1.get_balance():.2f}")

    account1.deposit(500)
    print(f"Balance after deposit: ${account1.get_balance():.2f}")

    try:
        account1.withdraw(1600)
        print(f"Balance: ${account1.get_balance():.2f}")
    except Exception as e:
        print(f"Insufficient funds: {e}")
        print(f"Final Balance: ${account1.get_balance():.2f}")
main()
