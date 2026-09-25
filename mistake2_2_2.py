from enum import Enum
from dataclasses import dataclass

class WordTier(Enum):
    STANDARD = "STANDARD"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

#Tạo một dataclass chỉ để chứa dữ liệu
@dataclass(frozen=True)
class TierConfig:
    discount_rate: float
    guest_passes: int

#Mapping từ Enum -> Config
TIER_CONFIGS = {
    WordTier.STANDARD: TierConfig(discount_rate=0.0, guest_passes=0),
    WordTier.GOLD: TierConfig(discount_rate=0.1, guest_passes=2),
    WordTier.PLATINUM: TierConfig(discount_rate=0.2, guest_passes=5),
}
class Member:
    def __init__(self, member_id: str, name: str, tier: WordTier):
        self.member_id = member_id
        self.name = name
        self.tier = tier

    @property
    def discount_rate(self):
        return TIER_CONFIGS[self.tier].discount_rate
    @property
    def guest_rate(self):
        return TIER_CONFIGS[self.tier].guest_passes
    
    def calculate_final_price(self, service_price: float) -> float:
        return service_price * (1 - self.discount_rate)

mem = Member("MB001", "Nguyễn Tú Uyên", tier=WordTier.GOLD)
print(mem.discount_rate)
print(mem.guest_rate)
print(mem.calculate_final_price(100))