from decimal import Decimal

# تصحيح الكلاس
class InvalidWithdrawel(Exception):
    def __init__(self, balance: Decimal, amount: Decimal, *args):
        super().__init__(f"Account doesn't have {amount}")
        self.balance = balance  # تصحيح الإملاء
        self.amount = amount

    def overage(self):  
        return self.amount - self.balance


def withdraw(balance: Decimal, amount: Decimal) -> Decimal:
    if amount > balance:
        raise InvalidWithdrawel(balance, amount)
    return balance - amount


try:
    balance = Decimal("100.00")
    withdrawal = Decimal("200.00")
    new_balance = withdraw(balance, withdrawal)  
    print(f"New balance: {new_balance}")
except InvalidWithdrawel as e:
    print(f"Error: {e}")
    print(f"You tried to withdraw {e.amount}, but balance is {e.balance}")
    print(f"Overage: {e.overage()}")