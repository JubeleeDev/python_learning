from types import NotImplementedType
from dataclasses import dataclass

@dataclass
class Transaction:
    account_owner: str
    amount: float
    kind: str

class ManualTransaction:
    def __init__(self, account_owner: str, amount: float, kind: str) -> None:
        self.account_owner = account_owner
        self.amount = amount
        self.kind = kind
    
    def __repr__(self) -> str:
        return f"ManualTransaction(account_owner='{self.account_owner}', amount={self.amount}, kind='{self.kind}')"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, ManualTransaction):
            return NotImplemented

        return self.account_owner == other.account_owner and self.kind == other.kind and self.amount == other.amount

if __name__ == "__main__":
    first_trans = Transaction("Lyla", 500, "deposit")
    second_trans = Transaction("Lyla", 500, "deposit")
    third_trans = Transaction("Eric", 50000, "withdraw")

    print(first_trans == second_trans)
    print(first_trans == third_trans)
    print(first_trans)