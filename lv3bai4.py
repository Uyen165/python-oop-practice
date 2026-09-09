import datetime

def add_timestamp(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.created_at = datetime.datetime.now() #create_at là thuộc tính thời gian
    cls.__init__ = new_init
    return cls

class Weapon:
    def __init__(self, name, damage):
        if not isinstance(name, str):
            raise TypeError("Vui lòng nhập đúng định dạng tên vũ khí!")
        self.name = name
        if not isinstance(damage, (int, float)) or isinstance(damage, bool):
            raise TypeError("Vui lòng nhập đúng định dạng số (Sát thương)")
        if damage < 0: raise ValueError("Vui lòng không nhập số âm (Sát thương)")
        self.damage = damage

    #self.__class__.__name__ là để lấy tên một Class dưới dạng chuỗi
    def __repr__(self):
        created_time = getattr(self, 'created_at', 'N/A')
        return f"{self.__class__.__name__}(name='{self.name}', damage={self.damage}, created_at='{created_time})"
@add_timestamp
class Sword(Weapon):
    def __init__(self, name, damage, length):
        super().__init__(name, damage)

        if not isinstance(length, (int, float)) or isinstance(length, bool):
            raise TypeError("Vui lòng nhập số (Chiều dài kiếm)!")
        self.length = length

@add_timestamp
class Bow(Weapon):
    def __init__(self, name, damage, range_distance):
        super().__init__(name, damage)

        if not isinstance(range_distance, (int, float)) or isinstance(range_distance, bool):
            raise TypeError("Vui lòng nhập số (Tầm bắn của cung)!")
        self.range_distance = range_distance

#Lớp này để người dùng tạo ra vũ khí, sau đó ta sử dụng if else để phân loại và trả về kiểu dữ liệu tương ứng
class WeaponFactory:
    @staticmethod
    def create_weapon(weapon_type, name, damage, extra_param):
        if not isinstance(weapon_type, str):
            raise TypeError("Loại vũ khí phải là chuỗi kí tự!")
        weapon_type_new = weapon_type.lower().strip()

        if weapon_type_new == "sword":
            return Sword(name=name, damage=damage, length=extra_param)
        elif weapon_type_new == "bow":
            return Bow(name=name, damage=damage, range_distance=extra_param)
        else:
            raise ValueError("Không tồn tại loại vũ khí này")

if __name__ == '__main__':
    w = WeaponFactory.create_weapon("sword", "Vũ khí 1", 2000, 100)
    print(w.created_at)
    print(w)