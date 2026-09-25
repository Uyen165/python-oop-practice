from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def get_balance(self) -> float:
        pass
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

class WithdrawableAccount(Account):
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass
#Các hàm cộng/trừ số dư chỉ thực hiện hành động làm thay đổi trạng thái, không dùng return
class StandardAccount(WithdrawableAccount):
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Số dư không đủ!")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance

class ReadOnlyAccount(Account):
    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, amount: float) -> None:
        self._balance += amount

    def get_balance(self) -> float:
        return self._balance

def transfer_interst(account: Account, interest: float):
     return account.deposit(interest)

if __name__ == "__main__":
     acc = StandardAccount(100)
     transfer_interst(acc, 12)
     print(f"Số dư mới: {acc.get_balance()}") #112