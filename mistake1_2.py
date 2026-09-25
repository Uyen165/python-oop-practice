from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

# 1. Đóng gói dữ liệu linh hoạt (Notification Object)
@dataclass(frozen=True)
class Notification:
    recipient: str                 # Người nhận (Email hoặc SĐT)
    body: str                      # Nội dung tin nhắn
    subject: Optional[str] = None  # Tiêu đề (Có thể có hoặc không)

# 2. Khung quy chuẩn (ABC Interface)
class BaseNotificationService(ABC):
    @abstractmethod
    def send(self, notification: Notification) -> None:
        """Mọi dịch vụ bắt buộc phải nhận duy nhất 1 gói Notification"""
        pass

# 3. Dịch vụ gửi Email (Tuân thủ ABC)
class EmailService(BaseNotificationService):
    def __init__(self, smtp_server: str, port: int):
        self.smtp_server = smtp_server
        self.port = port

    def send(self, notification: Notification) -> None:
        # Lấy subject từ gói dữ liệu, nếu không có thì dùng mặc định
        subject = notification.subject or "Thông báo từ hệ thống"
        print(f"[Email {self.smtp_server}:{self.port}] Gửi tới {notification.recipient} | Tiêu đề: {subject} | Nội dung: {notification.body}")

    def verify_smtp_connection(self) -> bool:
        print("SMTP Server hoạt động bình thường.")
        return True

# 4. Dịch vụ gửi SMS (Tuân thủ ABC)
class SMSService(BaseNotificationService):
    def __init__(self, provider_name: str):
        self.provider_name = provider_name

    def send(self, notification: Notification) -> None:
        # SMS chỉ dùng recipient và body, tự động bỏ qua subject mà không hề báo lỗi
        print(f"[SMS Provider: {self.provider_name}] Gửi tin nhắn tới {notification.recipient} | Nội dung: {notification.body}")

# 5. Lớp xử lý Chiến dịch (Dùng Composition & Dependency Injection)
class BlackFridayCampaign:
    # Đổi tên biến 'mess' -> 'notification_service' cho rõ nghĩa
    def __init__(self, notification_service: BaseNotificationService, campaign_name: str, discount_percent: int):
        self.notification_service = notification_service
        self.campaign_name = campaign_name
        self.discount_percent = discount_percent

    # Đổi tên biến 'customer_mess' -> 'recipients' (Danh sách người nhận)
    def run_campaign(self, recipients: list[str]):
        print(f"--- Bắt đầu chiến dịch: {self.campaign_name} (Giảm {self.discount_percent}%) ---")
        for target in recipients:
            # Tạo gói dữ liệu đóng gói Notification
            noti = Notification(
                recipient=target,
                subject=f"Ưu đãi {self.campaign_name}",
                body=f"Nhập mã BF{self.discount_percent} để được giảm giá!"
            )
            # Gửi gói dữ liệu qua dịch vụ được tiêm vào
            self.notification_service.send(noti)

# 6. Chạy thử nghiệm
if __name__ == "__main__":
    # --- Trường hợp 1: Chạy chiến dịch bằng EMAIL ---
    email_service = EmailService("smtp.gmail.com", 587)
    email_campaign = BlackFridayCampaign(email_service, "Sinh nhật Shopee", 30)
    email_campaign.run_campaign(["user1@gmail.com", "user2@gmail.com"])

    print("-" * 50)

    # --- Trường hợp 2: Chạy chiến dịch bằng SMS ---
    sms_service = SMSService("Viettel TeleCom")
    sms_campaign = BlackFridayCampaign(sms_service, "Siêu Sale SMS", 50)
    sms_campaign.run_campaign(["0987654321", "0912345678"])