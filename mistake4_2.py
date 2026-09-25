from typing import Protocol

class Writable(Protocol):
    def save(self, data: str) -> None: ...
class Readable(Protocol):
    def read(self) -> str: ...

class LocalStorage:
    def save(self, data: str) -> None:
        print(f"[Local Disk] Đã lưu dữ liệu: '{data}' vào file local.txt")
    def read(self) -> str:
        return "Nội dung file local.txt"
class AuditLogger:
    def save(self, data: str):
        print(f"[Audit Log] Đã ghi nhận vết hệ thống: '{data}'")

#Hàm dịch vụ đứng độc lập:
def backup_data(writer: Writable, data: str):
    writer.save(data)

if __name__ == "__main__":
    lst = LocalStorage()
    backup_data(lst, "NTU") #[Local Disk] Đã lưu dữ liệu: 'NTU' vào file local.txt
    print()
    adl = AuditLogger()
    backup_data(adl, "Nguyễn Tú Uyên") #[Audit Log] Đã ghi nhận vết hệ thống: 'Nguyễn Tú Uyên'
    print()
    print(lst.read()) #Nội dung file local.txt


    #Vẫn có thể gọi riêng như bình thường như sau:
    lst.save("Khoa") #[Local Disk] Đã lưu dữ liệu: 'Khoa' vào file local.txt
    #Tuy nhiên, gọi riêng dùng khi thao tác cục bộ, nhỏ lẻ
    #Còn hàm dịch vụ độc lập dùng để đóng gói quy trình nghiệp vụ chung, giúp hệ thống dễ mở rộng và dễ dàng viết Test