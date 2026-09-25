from enum import Enum

class WordStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

class Order:
    def __init__(self, order_id: str, total_amount: float, status: WordStatus):
        self.order_id = order_id
        self.total_amount = total_amount
        self.status = status
#Sử dụng property để vẫn giữ shipping_fee là thuộc tính của class (Ko cần khai báo trong init)
#Thay vì dùng hàm (vì không muốn truy cập như phương thức))
    @property
    def shipping_fee(self) -> float:
        if self.status in (WordStatus.PENDING, WordStatus.PROCESSING):
            return 30.0
        return 0.0


od = Order("U1605", 150.0, status = WordStatus.COMPLETED)
print(od.status) #WordStatus.COMPLETED
print(od.status.value) #COMPLETED
print(od.shipping_fee) #0.0