# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod

# 1. Tạo Interface đại diện cho tính năng "Chuyển thành JSON"
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass
        
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


# 2. Cho Circle ĐA KẾ THỪA từ cả GraphicShape lẫn JSONify
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    # Thực thi luật của GraphicShape
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    # 3. Thực thi luật của Interface JSONify (Viết hàm toJSON)
    def toJSON(self):
        return f"{{ 'Circle' : {str(self.calcArea())} }}"


# --- CHẠY THỬ ---
c = Circle(10)
print("Diện tích:", c.calcArea())
print("Chuỗi JSON:", c.toJSON())