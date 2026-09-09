# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)
    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if name == "price":
            if not isinstance(value, float):
                raise TypeError("Gía phải là số thực")
            if value < 0: raise ValueError("Gía phải lớn hơn 0")
        super().__setattr__(name, value)
    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return f"{name} không tồn tại!"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
print(b1.price)
print(b1.title)
#b1.price = 100 #TypeError: Gía phải là số thực
print(b2.power) #power không tồn tại!
