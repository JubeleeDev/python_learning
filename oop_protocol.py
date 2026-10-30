
from abc import ABC
from typing import Protocol
from abc import abstractmethod

from oop_inheritance import SavingsAccount, CreditAccount
from oop_demo import BankAccount

class SupportsWithdraw(Protocol):
    owner: str
    balance: float
    def withdraw(self, amount: float) -> None:
        ...

class Wallet:
    owner: str
    balance: float

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if self.balance - amount < 0:
            raise ValueError("not enough balance to withdraw")
        self.balance -= amount

class AbstractWallet(ABC):
    owner: str
    balance: float

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

class WithdrawWallet(AbstractWallet):
    def __init__(self, owner: str, balance: float) -> None:
        super().__init__(owner, balance)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if self.balance - amount < 0:
            raise ValueError("not enough balance to withdraw")
        self.balance -= amount

def withdraw_from_all(accounts: list[SupportsWithdraw], amount: float) -> None:
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

    wallet = Wallet("Lusia", 2000)

    withdraw_wallet = WithdrawWallet("testABC", 1000)

    saving_acc.add_interest()
    print(f"saving acc balance is {saving_acc.balance}")

    withdraw_from_all([bank_acc, saving_acc, credit_acc, wallet, withdraw_wallet], 1200)