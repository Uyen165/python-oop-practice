def make_scaler(multiplier, offset):
    def scale_list(data_list):
        result = []
        for x in data_list:
            y = (x * multiplier) + offset
            result.append(y)
        return result
    return scale_list
# - Công cụ A: Nhân 2 rồi cộng 5
scale_A = make_scaler(multiplier=2, offset=5)

# - Công cụ B: Nhân 0.5 rồi trừ 10 (cộng -10)
scale_B = make_scaler(multiplier=0.5, offset=-10)

# 3. Test với dữ liệu:
data = [10, 20, 30]
# In ra kết quả scale_A(data)  -> Kỳ vọng: [25, 45, 65]
print(scale_A(data))
# In ra kết quả scale_B(data)  -> Kỳ vọng: [-5.0, 0.0, 5.0]
print(scale_B(data))