from typing import Union

class AtmAccount:

    available_account = 9991

    def __init__(self, holder) -> object:
        self.__balance = 0.0 #  _ protected
        self.__holder = holder  # __ private
        self.__account_number = AtmAccount.available_account
        AtmAccount.available_account += 1

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def _balance(self, amount: Union[int, float]) -> None:
        self.__balance = amount

    def deposit(self, amount: Union[int, float]) -> None:
        self._balance += amount

    def withdraw(self, amount: Union[int, float]) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


account1 = AtmAccount('Yossi Eik')

account1.deposit(100)
print(account1.balance)

account1.withdraw(100)
print(account1.balance)
