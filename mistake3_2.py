from abc import ABC, abstractmethod

class PointStrategy(ABC):
    @abstractmethod
    def calculate_points(self, price: float) -> float:
        pass
class StandardPointStrategy(PointStrategy):
    def calculate_points(self, price):
        return int(price * 0.05)
class VIPPointStrategy(PointStrategy):
    def calculate_points(self, price):
        return int(price * 0.1)
class StudentPointStrategy(PointStrategy):
    def calculate_points(self, price):
        return 20

class MovieTicket:
    def __init__(self, movie_name: str, price: float, point: PointStrategy):
        self.movie_name = movie_name
        self.price = price
        self.point = point
    def get_point(self):
        p = self.point.calculate_points(self.price)
        return p
    def get_description(self):
        return f"Thông tin phim: {self.movie_name}, Giá: {self.price}, Điểm thưởng: {self.get_point()}"
if __name__ == "__main__":
    m = MovieTicket("Xác ướp Ai Cập", 120.0, point=StudentPointStrategy())
    print(m.get_point()) #20
    print(m.get_description()) #Thông tin phim: Xác ướp Ai Cập, Giá: 120.0, Điểm thưởng: 20