class FeatureScaler:

    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def get_standardizer(self):
        # Hàm con mượn thuộc tính/biến của phương thức cha
        m = self.mean
        s = self.std

        def standardize(x):
            return (x - m) / s

        return standardize
scaler = FeatureScaler(mean=10, std=2) 
#m chỉ là một biến chụp lại giá trị 10 tại thời điểm hàm get_standardizer đc gọi
standard_func = scaler.get_standardizer()
print(standard_func.__code__.co_freevars) #('m', 's')
print(standard_func.__closure__)
print(standard_func(20)) #5.0
#<cell at 0x0000010B7E95B9A0: int object at 0x00007FFEFAEC7448>, <cell at 0x0000010B7E95B970: int object at 0x00007FFEFAEC7348>)
scaler.mean = 100 #Khi này, m nằm trong Cell Object không còn dính dáng gì tới mean
print(standard_func(20)) #Dù có vô tình đổi kết quả vẫn như cũ (5.0)
print(standard_func.__closure__[0].cell_contents) #10 (Kết quả của mean vẫn là 10, không phải 100)