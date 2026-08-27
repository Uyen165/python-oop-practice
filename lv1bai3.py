class BankAccount:
    BANK_NAME = "Vietcombank"

    def __init__(self, account_number:str, owner_name:str, balance:float):
        self.account_number = account_number
        self.owner_name = owner_name
        if balance < 0:
            raise ValueError("Số dư ban đầu không được âm!")
        self._balance = balance #Ở đây vì đã check logic ở ngay hàm init (và không có hàm setter) nên ta có thể gán self._balance = balance (gán trực tiếp)

    @property
    def balance(self):
        return self._balance

    #Nạp tiền
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền phải lớn hơn 0")
        else:
            self._balance += amount

    #Rút tiền
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0!")
        if amount > self._balance:
            raise ValueError("Số dư không đủ!")
        self._balance -= amount

    def enable_overdraft(self, limit):
        if limit < 0:
            raise ValueError("Hạn mức thấu chí không được bé hơn 0")
        else:
            self._overdraft_limit = limit

    def get_total_available_credit(self):
        if hasattr(self, "_overdraft_limit"):
            return self._balance + self._overdraft_limit
        else:
            return self._balance

    def __repr__(self):
        return f"BankAccount(account_number='{self.account_number}', owner_name='{self.owner_name}', balance={self.balance})"

if __name__ == '__main__':
    nh1 = BankAccount("3337391206", "Nguyen Tu Uyen", 100.0)
    print(nh1) #BankAccount(account_number='3337391206', owner_name='Nguyen Tu Uyen', balance=100.0)
    nh1.deposit(10)
    print(nh1) #BankAccount(account_number='3337391206', owner_name='Nguyen Tu Uyen', balance=110.0)
    nh1.withdraw(20)
    print(nh1) #BankAccount(account_number='3337391206', owner_name='Nguyen Tu Uyen', balance=90.0)
    nh1.enable_overdraft(50)
    print(nh1.get_total_available_credit()) #140.0
    print(nh1) #BankAccount(account_number='3337391206', owner_name='Nguyen Tu Uyen', balance=90.0)
    print(nh1.balance) #@property dù ko có setter vẫn đảm bảo việc tránh truy cập trực tiếp vào _balance

    #Ta return ở hàm get_total_available_credit để đảm bảo tính rành mạch, không thay đổi số dư gốc (mang tính trường hợp đặc biệt)
    #Ta thay đổi/gán trực tiếp self._balance ở các hàm rút tiền, nạp tiền thì nó sẽ thay đổi số dư gốc