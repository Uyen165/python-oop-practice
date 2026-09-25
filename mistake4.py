from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self): pass
class GasolineRefuelable(ABC):
    @abstractmethod
    def refuel_gasoline(self): pass
class ElectricChargeable(ABC):
    @abstractmethod
    def charge_battery(self): pass

class GasolineCar(Movable, GasolineRefuelable):
    def move(self): print("Xe chạy bằng động cơ đốt trong")
    def refuel_gasoline(self): print("Đổ xăng 95")
class ElectricScooter(Movable, ElectricChargeable):
    def move(self): print("Xe điện di chuyển")
    def charge_battery(self): print("Cắm sạc 220V") 

if __name__ == "__main__":
    car = GasolineCar()
    car.move()
    car.refuel_gasoline()
    print()
    scooter = ElectricScooter()
    scooter.move()
    scooter.charge_battery()
