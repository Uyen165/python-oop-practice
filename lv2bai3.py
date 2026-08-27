class Logger:
    def log(self, message:str):
        return f"[LOG]: {message}"
    
class Validator:
    def validate_positive(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Gia trị phải là số!")
        if value <= 0:
            raise ValueError("Gía trị phải lớn hơn 0!")

class SmartWallet(Logger, Validator):
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Số dư phải lớn hơn 0")
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    #Thắc mắc 1: Khi kế thừa, có thể truy cập hàm qua self mà không cần ghi super à?
    def deposit(self, amount):
        self.validate_positive(amount)
        self._balance += amount
        return self.log(f"Đã nạp {amount} VNĐ vào ví")

    def withdraw(self, amount):
        self.validate_positive(amount)
        if amount > self._balance: raise ValueError("Số dư không đủ")
        self._balance -= amount
        return self.log(f"Đã rút {amount} VNĐ khỏi ví.")

    def __repr__(self):
        return f"SmartWallet(owner='{self.owner}', balance={self.balance})"

if __name__ == '__main__':
    v1 = SmartWallet("Nguyễn Tú Uyên", 500000)
    print(v1)

    n = v1.deposit(20000)
    print(v1)
    print(n)

    m = v1.withdraw(200000)
    print(v1)
    print(m)

    print(SmartWallet.__mro__)