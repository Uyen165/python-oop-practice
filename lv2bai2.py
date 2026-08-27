class Account:
    def __init__(self, account_id:str, balance:float):
        self.account_id = account_id

        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise TypeError("Số dư phải là số thực/ số nguyên!")
        if balance < 0:
            raise ValueError("Số dư không được là số âm")
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount:float):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Số tiền nạp vào phải là một số thực/số nguyên")
        if amount <= 0:
            raise ValueError("Số tiền nạp vào phải lớn hơn 0")
        self._balance += amount

    def withdraw(self, amount:float):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Số tiền rút phải là một số thực/số nguyên")
        if amount <= 0 or amount > self._balance:
            raise ValueError("Số dư không đủ/không hợp lệ!")
        self._balance -= amount

    def __repr__(self):
        return f"Account(account_id='{self.account_id}', balance={self.balance})"

class SavingsAccount(Account):
    def __init__(self, account_id:str, balance:float, interest_rate:float):
        super().__init__(account_id, balance)

        if not isinstance(interest_rate, (int, float)) or isinstance(interest_rate, bool):
            raise TypeError("Lãi suất phải là số thực/số nguyên")
        if interest_rate < 0.0 or interest_rate > 0.2:
            raise ValueError("Lãi suất không hợp lệ (tối đa 20%)")
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

    def withdraw(self, amount):
        total_deduct = amount * 1.02
        super().withdraw(total_deduct)

    def __repr__(self):
        return f"SavingsAccount(account_id='{self.account_id}', balance={self.balance}, interest_rate={self.interest_rate})"

if __name__ == '__main__':
    acc1 = Account("3337391206", 500000)
    print(acc1)
    print(acc1.balance)
    acc1.deposit(100000)
    print(acc1)
    acc1.withdraw(50000)
    print(acc1)

    acc2 = SavingsAccount("3337391206", 100000000, 0.1)
    print(acc2)
    acc2.apply_interest()
    print(acc2)
    acc2.withdraw(200000)
    print(acc2)