class LibraryBook:
    BOOK_CATEGORIES = ("FICTION", "EDUCATIONAL", "NON-FICTION")

    def __init__ (self, title, author, price):
        self.title = title
        self.author = author
        self.price = price #Goi qua property ngay tu dau

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Loi: Gia sach phai lon hon 0!")

    def apply_discount(self, percent):
        if 0 <= percent <= 100: 
            self._discount = percent
        else:
            raise ValueError("Phan tram giam gia phai tu 0 - 100")

    def get_final_price(self) -> float:
        if hasattr(self, "_discount"):
            return self.price * (1 - self._discount / 100)
        return self.price

    @classmethod
    def get_book_categories(cls) -> tuple:
        return cls.BOOK_CATEGORIES

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        if not isinstance(isbn, str):
            return False

        clean_isbn = isbn.replace("-", "").replace(" ", "")

        #Dong nay gop 2 dieu kien kiem tra
        return len(clean_isbn) in (10, 13) and clean_isbn.isdigit()

    def __repr__(self):
        return f"LibraryBook (title = '{self.title}', author = '{self.author}', price = {self.price})"

if __name__ == "__main__":
    print(LibraryBook.is_valid_isbn("123-456-12-04-0"))
    print(LibraryBook.is_valid_isbn("1605"))

    b1 = LibraryBook("Data Science", "Tu Uyen", 150.0)
    b2 = LibraryBook("Data", "Uyen", 200.0)

    b1.apply_discount(20)

    print(b1.get_final_price())

    list_books = [b1, b2]
    print(list_books)