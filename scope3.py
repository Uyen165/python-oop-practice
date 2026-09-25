#Cach 1
def train_model():
    print("Đang huấn luyện mô hình AI...")
def my_logger(func):
    def wrapper():
        print("[LOG] Bắt đầu tiến trình...")
        func()
        print("[LOG] Hoàn tất tiến trình thành công!")
    return wrapper
train = my_logger(train_model)
train()
