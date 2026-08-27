class Product:
    DISCOUNT_LIMIT = 0.5

    def __init__(self, name, price):
        self.name = name

        #Có thể ép validation ngay từ hàm init như sau (hoặc có thể chỉ để Setter làm nơi check lỗi duy nhất)
        if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
            raise ValueError("Gia ca phai la mot so nguyen hoac so thuc!")
        self.price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Gia ca phai lon hon 0!")
        else:
            self._price = new_price

    def set_discount(self, rate):
        if 0 <= rate <= Product.DISCOUNT_LIMIT :
            self._discount = rate
        else:
            raise ValueError("Muc giam gia khong hop le!")

    def get_final_price(self):
        if hasattr(self, "_discount"):
            return self.price * (1 - self._discount)
        else:
            return self.price

    def __repr__(self):
        return f"Product(name = '{self.name}', price = {self.price})"

if __name__ == '__main__':
    p1 = Product("Banh mi", 100)
    print(p1)
    p1.set_discount(0.2)
    print(p1.get_final_price())