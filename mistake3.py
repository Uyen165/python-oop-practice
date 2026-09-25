from dataclasses import dataclass
@dataclass(frozen=True)
class ServiceAddon:
    name: str
    price: float

#KHAI BÁO CÁC DỊCH VỤ CÓ SẴN (Gía cố định của khách sạn)
BREAKFAST = ServiceAddon(name="Ăn sáng", price=15.0)
AIRPORT_PICKUP = ServiceAddon(name="Đón sân bay", price=30.0)
LAUNDRY = ServiceAddon(name="Giặt ủi", price=10.0)

class Room:
    def __init__(self, room_number: str, base_price: float, addons: list[ServiceAddon] = None):
        self.room_number = room_number
        self.base_price = base_price
        self.addons = addons or []
    def get_total_price(self) -> float:
        return self.base_price + sum(s.price for s in self.addons)

    def get_description(self) -> str:
        if not self.addons:
            return f"Phòng {self.room_number} (Không dịch vụ thêm)"
        addon_names = ", ".join(s.name for s in self.addons)
        return f"Phòng {self.room_number} (Kèm: {addon_names})"

if __name__ == "__main__":
    r = Room("R101", 300.0, addons=[BREAKFAST, AIRPORT_PICKUP])
    print(r.get_total_price())
    print(r.get_description())
    print(f"Tổng tiền: ${r.get_total_price()}")
#Output
#345.0
#Phòng R101 (Kèm: Ăn sáng, Đón sân bay)
#Tổng tiền: $345.0

