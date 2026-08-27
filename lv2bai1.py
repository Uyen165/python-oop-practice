class LibraryCard:
    __card_counter = 1000
    def __init__(self, owner_name:str):
        self.owner_name = owner_name
        self._card_id = f"LIB-{LibraryCard.__card_counter}"
        #Tăng mã biến đếm của Class lêm 1 cho thẻ tiếp theo
        LibraryCard.__card_counter += 1
        self._balance = 0.0

    @property
    def card_id(self):
        return self._card_id

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Vui lòng nạp tiền > 0 đồng")
        else:
            self._balance += amount

    def deduct(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Số dư không đủ")

    def swipe(self):
        #self._balance -= 10000
        #Không nên viết như trên trừ trực tiếp, mà ta gọi hàm deduct để kiểm tra đủ số dư rồi mới trừ
        self.deduct(10000)
        return f"Thẻ {self.card_id} của {self.owner_name} đã thanh toán thành công!"

class EWallet:
    def swipe(self):
        return f"Ví điện tử thanh toán thành công!"

def process_entry(payment_method):
    #Truyền đúng 2 tham số: đối tượng & tên phương thức
    #Hàm callable(x) để kiểm tra xem biến x có phải là một thứ có thể gọi/thực thi đc không (như hàm, phương thức, có thể dùng dấu())
    if hasattr(payment_method, "swipe") and callable(getattr(payment_method, "swipe")):
        return payment_method.swipe()
    else:
        raise RuntimeError("Phương thức thanh toán không hợp lệ!")

if __name__ == '__main__':
    kh1 = LibraryCard("Nguyễn Tú Uyên")
    kh2 = LibraryCard("Phạm Nguyễn Trường Giang")
    print(kh1.card_id)
    print(kh2.card_id)

    kh1.deposit(5000000)
    kh2.deposit(1000000)
    print(kh1.balance)
    print(kh2.balance)

    kh1.deduct(30)
    kh2.deduct(10)
    print(kh1.balance)
    print(kh2.balance)

    print(kh1.swipe())
    print(kh2.swipe())

    kh3 = EWallet()
    print(kh3.swipe())

    kq = process_entry(kh2)
    print(kq)
