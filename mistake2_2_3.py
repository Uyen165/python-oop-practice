from enum import Enum

#STANDARD, GOLD, PLATINUM đã đóng luôn vai trò làm Tên nhãn (Name) của Enum
class WordTier(Enum):
    STANDARD = (0.0, 0)
    GOLD = (0.1, 2)
    PLATINUM = (0.2, 5)

    @property
    def discount_rate(self) -> float:
        return self.value[0]

    @property
    def guest_passes(self) -> int:
        return self.value[1]

class Member:
    def __init__(self, member_id: str, name: str, tier: WordTier):
        self.member_id = member_id
        self.name = name
        self.tier = tier

    #Gọi discount_rate từ thuộc tính tier (là WordTier)
    def calculate_final_price(self, service_price: float) -> float:
        return service_price * (1 - self.tier.discount_rate)

mem = Member("MB001", "Nguyễn Tú Uyên", tier=WordTier.GOLD)
#Khi truy cập vào thuộc tính phải qua tier (vì những thuộc tính cần truy cập đó là thuộc tính của WordTier)
print(mem.tier.name) #GOLD
print(mem.tier.discount_rate) #0.1
print(mem.tier.guest_passes) #2
print(mem.member_id) #Đây là thuộc tính của class Member nên không cần qua tier
print(mem.calculate_final_price(100)) #90.0