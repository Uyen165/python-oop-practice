def create_counter(start_value=0):
    
    def count_up():
        nonlocal start_value
        start_value += 1
        return start_value
    return count_up

counter_A = create_counter(start_value = 20)
print(counter_A()) #21
print(counter_A()) #22
counter_B = create_counter()
print(counter_B()) #1
print(counter_B()) #2

#nonlocal cho Python biết rằng start_value trong count_up() không phải là biến local mới, mà là biến thuộc scope của hàm bên ngoài create_counter(), và cho phép ta gán/thay đổi giá trị của biến đó.