from enum import Enum

class WordTier(Enum):
    STANDARD = "STANDARD"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

class Member:
    def __init__(self, member_id: str, name: str, tier: WordTier):
        self.member_id = member_id
        self.name = name
        self.tier = tier
    @property
    def discount_rate(self):
        if self.tier == WordTier.STANDARD:
            return 0.0
        elif self.tier == WordTier.GOLD:
            return 0.1
        else: return 0.2
    @property
    def guest_passes(self):
        if self.tier == WordTier.STANDARD:
            return 0
        elif self.tier == WordTier.GOLD:
            return 2
        else: return 5

    def calculate_final_price(self, service_price: float) -> float:
        return service_price * (1 - self.discount_rate)

mem = Member("MB001", "Nguyễn Tú Uyên", tier=WordTier.GOLD)
print(mem.discount_rate)
print(mem.guest_passes)
print(mem.calculate_final_price(100))