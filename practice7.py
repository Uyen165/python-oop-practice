class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __getattribute__(self, name):
        # Nếu người dùng hỏi lấy 'price', tự động trả về giá đã giảm 30%
        if name == "price":
            raw_price = super().__getattribute__("price") #Lấy giá gốc
            return raw_price * 0.9 #Trả về giá đã giảm

        #Các thuộc tính khác (title) thì trả về bình thường
        return super().__getattribute__(name)

b1 = Book("DS", 100.0)
print(b1.title) #DS
print(b1.price) #90.0