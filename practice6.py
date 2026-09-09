#__setattr__
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def __setattr__(self, name, value):
        if name == "price":
            if not isinstance(value, float):
                raise TypeError("Gía sách phải là kiểu float")
        super().__setattr__(name, value)
b1 = Book("DS", 100.0)
b1.price = 100 #TypeError: Gía sách phải là kiểu float