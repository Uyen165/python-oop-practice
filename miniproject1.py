from dataclasses import dataclass, field
from abc import ABC, abstractmethod
@dataclass(frozen=True)
class Transaction:
    transaction_id: str
    customer_id: str
    amount: float
    items: list[str]
    status: str = field(default="COMPLETED")

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Dữ liệu đầu vào không hợp lệ!")
        #Mẹo bypass ghi đè thuộc tính khi dùng frozen=True
        object.__setattr__(self, "items", tuple(self.items))

class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, record: Transaction) -> Transaction:
        pass

class AmountDiscountTransformer(BaseTransformer):
    def transform(self, record):
        if record.amount > 500:
            discount_amount = record.amount - (record.amount * 0.1)
        else:
            discount_amount = record.amount
        return Transaction(transaction_id=record.transaction_id, customer_id=record.customer_id, amount=discount_amount, items=record.items, status=record.status)

class StatusFilterTransformer(BaseTransformer):
    def transform(self, record):
        if record.status == "COMPLETED":
            return Transaction(transaction_id=record.transaction_id, customer_id=record.customer_id, amount=record.amount, items=record.items, status=record.status)
        else:
            return None
@dataclass
class PipelineComposer:
    transformers: list[BaseTransformer]

    def add_transformer(self, transformer: BaseTransformer):
        self.transformers.append(transformer)

    def __call__(self, record: Transaction) -> Transaction:
        for transformer in self.transformers:
            record = transformer.transform(record)
            if record is None: return None
        return record

class DataLoader:
    def __init__(self, raw_data_list: list[dict]):
        self.raw_data_list = raw_data_list
    @classmethod
    def from_csv_mock(cls, raw_data_list: list[dict]):
        return cls(raw_data_list)

    def stream_records(self):
        ids = set()

        for row in self.raw_data_list:
            t_id = row["transaction_id"]
            #Nếu id đã xuất hiện rồi thì bỏ qua
            if t_id in ids:
                continue
            #Nếu là ID mới: Lưu vào set
            ids.add(t_id)

            #Chuyển đổi từ dict thô sang @dataclass Transaction
            record = Transaction(transaction_id=row["transaction_id"], customer_id=row["customer_id"], amount=row["amount"], items=row["items"])
            yield record

class CustomerAnalytics:
    def __init__(self, customer_id: str, total_spent: float = 0.0):
        self.customer_id = customer_id
        self.total_spent = total_spent

    def add_transaction(self, record:Transaction):
        self.total_spent += record.amount

    def __eq__(self, other) -> bool:
        if not isinstance(other, CustomerAnalytics):
            return False
        return self.customer_id == other.customer_id

    def __lt__(self, other) -> bool:
        if not isinstance(other, CustomerAnalytics):
            return NotImplemented #Nó thường được dùng để báo hiệu rằng một phép toán hoặc một phương thức so sánh chưa được hỗ trợ (chưa được thiết lập) giữa hai đối tượng với nhau.
        return self.total_spent < other.total_spent

    def __repr__(self):
        return f"CustomerAnalytics(id='{self.customer_id}', spent={self.total_spent})"

if __name__ == '__main__':
    #Khai báo dữ liệu thô
    RAW_DATA = [
    {"transaction_id": "T001", "customer_id": "C101", "amount": 600.0, "items": ["Laptop", "Mouse"]},
    {"transaction_id": "T002", "customer_id": "C102", "amount": 150.0, "items": ["Keyboard"]},
    {"transaction_id": "T001", "customer_id": "C101", "amount": 600.0, "items": ["Laptop", "Mouse"]}, 
    {"transaction_id": "T003", "customer_id": "C103", "amount": 50.0, "items": ["Monitor"]},     
    {"transaction_id": "T004", "customer_id": "C101", "amount": 200.0, "items": ["Headphones"]},
    ]
    #Khởi tạo Bộ nạp dữ liệu (DATALOADER)
    loader = DataLoader.from_csv_mock(RAW_DATA)
    #Không gọi hàm stream_records ngay để bảo đảm tính "chờ đến khi cần mới làm" của yield
    composer = PipelineComposer(transformers=[StatusFilterTransformer(), AmountDiscountTransformer()])
    analytics_map: dict[str, CustomerAnalytics] = {} #Gợi ý str là mã khách hàng và CustomerAnalytics là chứa tổng tiền spent

    for record in loader.stream_records():
        clean_record = composer(record)

        if clean_record is not None:
            c_id = clean_record.customer_id

            #Nếu chưa có trong sổ -> Tạo tài khoản khách hàng mới
            if c_id not in analytics_map:
                analytics_map[c_id] = CustomerAnalytics(customer_id=c_id)
            #Cộng dồn tiền hóa đơn đã giảm giá
            analytics_map[c_id].add_transaction(clean_record)

    sorted_customers = sorted(analytics_map.values(), reverse=True)
    print("BẢNG XẾP HẠNG KHÁCH HÀNG CHI TIÊU")
    #enumerate là để vừa lấy phần tử trong danh sách, vừa tự động đánh số thứ tự (đếm số) cho phần tử đó.
    for rank, customer in enumerate(sorted_customers, 1):
        print(f"Hạng {rank}: {customer}")

