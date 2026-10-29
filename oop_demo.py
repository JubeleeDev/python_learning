
class BankAccount:
    
    bank_name: str = "LearnBank"

    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        elif (self.balance - amount) < 0:
            raise ValueError("balance is not enough to withdraw")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance

if __name__ == "__main__":
    first_acc = BankAccount("Alex", 100)
    second_acc = BankAccount("Matthew", 1000)

    first_acc.deposit(500)
    second_acc.withdraw(500)

    print(f"first account info: owner = {first_acc.owner} balance={first_acc.get_balance()}, {first_acc.bank_name}")
    print(f"second account info: owner = {second_acc.owner} balance={second_acc.get_balance()}, {second_acc.bank_name}")

    first_acc.bank_name = "HackBank"

    print(f"first account bank is {first_acc.bank_name}")
    print(f"second account bank is {second_acc.bank_name}")
    print(f"class account bank is {BankAccount.bank_name}")