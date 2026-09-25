#Cach 2
def my_logger(func):
    def wrapper():
        print("[LOG] Bắt đầu tiến trình...")
        func()
        print("[LOG] Hoàn tất tiến trình thành công!")
    return wrapper
@my_logger
def train_model():
    print("Đang huấn luyện mô hình AI...")
train_model()