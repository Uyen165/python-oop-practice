# Python code​​​​​‌​​​​​​‌‌‌​‌‌‌​‌‌​‌‌‌​‌​​‌ below
# Use print("messages...") to debug your solution.
from dataclasses import dataclass

show_expected_result = False
show_hints = False

@dataclass(eq = False) #Yeu cau khong so sanh == giữa Stock & Bond
class Asset():
    price: float
    #Các hàm tại lớp cơ sở(cha), sẽ giúp lớp con có thể tự so sánh giữa chúng, và so sánh giữa các lớp con
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
@dataclass #Để vẫn có thể so sánh == trong nội bộ đối tượng Stock
class Stock(Asset):
    ticker: str
    company: str
@dataclass #Để vẫn có thể so sánh == trong nội bộ đối tượng Bond
class Bond(Asset):
    description: str
    duration: int
    interest: float

s1 = Stock(12.0, "Ve", "Cortis")
s2 = Stock(15.0, "Ve2", "Cortis")
s3 = Stock(12.0, "Ve", "Cortis")

print(s1 == s3) #True
print(s1>s2) #False
b1 = Bond(15.0, "Ve concert", 2, 0.5)
b2 = Bond(15.0, "Ve concert", 2, 0.5)

print(b1 >= s2) #True
print(b1 == b2) #True