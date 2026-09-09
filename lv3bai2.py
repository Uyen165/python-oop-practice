import math
class Vector2D:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise TypeError("Định dạng số không hợp lệ!")
        self.x = x
        if not isinstance(y, (int, float)) or isinstance(y, bool):
            raise TypeError("Định dạng số không hợp lệ!")
        self.y = y

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    #Khi muốn gọi hàm, ta chỉ cần truyền vào dấu +
    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Chỉ có thể cộng 2 Vector 2D với nhau!")
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector2D(new_x, new_y) #Trả về một đối tượng Vector 2D mới

    #Khi muốn gọi hàm, ta chỉ cần truyền vào dấu ==
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    #Khi muốn gọi hàm, ta chỉ cần len(obj)
    def __len__(self):
        return round(math.sqrt(pow(self.x, 2) + pow(self.y, 2)))
    
if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(1, 2)
    print(len(v1))
    print(v2.__len__())
    print(v1 + v2)
    print(v1 == v2)

    v3 = Vector2D(2, 2)
    v4 = Vector2D(2, 2)
    print(v3 == v4) #Truyền vào dấu ==
    print(v3 + v4) #Truyền vào dấu +

    v5 = Vector2D(2.5, 1.2)
    print(len(v5)) 
