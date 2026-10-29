from oop_demo import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float) -> None:
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def __str__(self) -> str:
        return f"Saving account. Owner: {self.owner}, balance is {self.balance}, interest rate is {self.interest_rate}"

    def __repr__(self) -> str:
        return f"SavingAccount(owner='{self.owner}', balance={self.balance}, interest_rate={self.interest_rate})"

    def add_interest(self) -> None:
        self.balance += (self.balance * self.interest_rate)

class CreditAccount(BankAccount):
    def __init__(self, owner: str, balance: float, credit_limit: float) -> None:
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def __str__(self) -> str:
        return f"Credit account. Owner: {self.owner}, balance is {self.balance}, credit limit is {self.credit_limit}"

    def __repr__(self) -> str:
        return f"CreditAccount(owner='{self.owner}', balance={self.balance}, credit_limit={self.credit_limit})"

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        elif (self.balance - amount) < (self.credit_limit * -1):
            raise ValueError("balance must be higher than negative credit limit")
        self.balance -= amount

def withdraw_from_all(accounts: list[BankAccount], amount: float) -> None:
    for account in accounts:
        try:
            account.withdraw(amount)
            print(f"Withdraw is successful. New balance for {account.owner} is {account.balance}")
        except ValueError as e:
            print("Withdraw error:", e)


if __name__ == "__main__":
    bank_acc = BankAccount("John", 1000)
    saving_acc = SavingsAccount("John", 1000, 0.05)
    credit_acc = CreditAccount("John", 1000, 1500)

    saving_acc.add_interest()
    print(f"saving acc balance is {saving_acc.balance}")

    withdraw_from_all([bank_acc, saving_acc, credit_acc], 1200)