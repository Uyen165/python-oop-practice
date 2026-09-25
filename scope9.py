class CacheResult:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, x):
        if x in self.cache:
            print (f"[CACHE HIT] Lấy kết quả cho x={x}")
            return self.cache[x] #Trả về kết quả đã lưu, không tính lại
        else:
            print (f"[COMPUTE] Đang tính toán cho x={x}...")
            result = self.func(x)
            self.cache[x] = result
            return result
@CacheResult
def heavy_computation(n):
    return n * n * n

# Chạy lần 1 với n=4 -> Phải in [COMPUTE] và trả về 64
print(heavy_computation(4))

# Chạy lần 2 với n=4 -> Phải in [CACHE HIT] và trả về 64 ngay lập tức!
print(heavy_computation(4))

# Chạy lần 3 với n=5 -> Phải in [COMPUTE] và trả về 125
print(heavy_computation(5))