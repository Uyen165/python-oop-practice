#"Bộ Đếm Method" trong OOP
#Lưu ý rằng đây decorator cho hàm (ko phải decorator cho class)
def count_call(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"[LOG] Phương thức {func.__name__} đã chạy {count} lần")
        return func(*args, **kwargs)
    return wrapper
class DataProcessor:
    def __init__(self, name):
        self.name = name
    @count_call
    def clean_data(self, data):
        print(f"-> [self.__name__] Đang xử lý...")
c = DataProcessor("Uyen")
c.clean_data("Tap du lieu 1")
c.clean_data("Tap du lieu 2")