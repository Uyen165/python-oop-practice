from abc import ABC, abstractmethod

class Taxable(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass
class Employee(ABC):
    def __init__(self, emp_id: str, name: str, base_salary: float):
        if not isinstance(emp_id, str):
            raise TypeError("Định dạng ID không hợp lệ!")
        self._emp_id = emp_id
        if not isinstance(name, str):
            raise TypeError("Vui lòng nhập đúng định dạng họ tên")
        self._name = name
        if not isinstance(base_salary, (int, float)) or isinstance(base_salary, bool):
            raise TypeError("Vui lòng nhập lúc định dạng tiền lương")
        if base_salary < 0:
            raise ValueError("Tiền lương phải lớn hơn 0")
        self._base_salary = base_salary

    @property
    def emp_id(self): return self._emp_id
    @property
    def name(self): return self._name
    @property
    def base_salary(self): return self._base_salary

    @abstractmethod
    def calculate_monthly_pay(self):
        pass

    def __repr__(self):
        return f"Employee(emp_id='{self.emp_id}', name='{self.name}', base_salary={self.base_salary})"

class SalariedEmployee(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, bonus: float):
        super().__init__(emp_id, name, base_salary)
        if not isinstance(bonus, (int, float)) or isinstance(bonus, bool):
            raise TypeError("Tiền thưởng cố định định dạng không hợp lệ")
        if bonus < 0: raise ValueError("Tiền thưởng cố định phải >= 0")
        self.bonus = bonus

    def calculate_monthly_pay(self):
        return self.base_salary + self.bonus
    def __repr__(self):
        return f"SalariedEmployee(emp_id='{self.emp_id}', name='{self.name}', base_salary={self.base_salary}, bonus={self.bonus})"
    
class CommissionEmployee(Employee, Taxable):
    def __init__(self, emp_id: str, name: str, base_salary: float, sales_volume: float, commission_rate: float):
        super().__init__(emp_id, name, base_salary)
        if not isinstance(sales_volume, (int, float)) or isinstance(sales_volume, bool):
            raise TypeError("Định dạng doanh số không hợp lệ!")
        if sales_volume < 0: raise ValueError("Doanh số không được bé hơn 0")
        self.sales_volume = sales_volume
        if not isinstance(commission_rate, (int, float)) or isinstance(commission_rate, bool):
            raise TypeError("Tỷ lệ hoa hồng phải là một số thực!")
        if commission_rate < 0.0 or commission_rate > 1.0:
            raise ValueError("Tỷ lệ hoa hồng phải từ 0 - 1")
        self.commission_rate = commission_rate

    def calculate_monthly_pay(self):
        return self.base_salary + (self.sales_volume * self.commission_rate)

    def calculate_tax(self):
        # Thuế 10% chỉ tính trên PHẦN VƯỢT QUÁ 11,000,000
        monthly_pay = self.calculate_monthly_pay()
        if monthly_pay > 11000000:
            return (monthly_pay - 11000000) * 0.1
        else:
            return 0

    def total_calculate(self):
        return self.calculate_monthly_pay() - self.calculate_tax()

    def __repr__(self):
        return f"CommissionEmployee(emp_id='{self.emp_id}', name='{self.name}', base_salary={self.base_salary}, sales_volume={self.sales_volume}, commission_rate={self.commission_rate})"

if __name__ == '__main__':
    e1 = SalariedEmployee('24103100165', 'Nguyễn Tú Uyên', 10000000, 500000)
    print(e1)
    print(e1.calculate_monthly_pay())

    e2 = CommissionEmployee('24103100130', 'Trần Đình Bắc', 20000000, 1000000, 0.05)
    print(e2)
    print(e2.calculate_monthly_pay())
    print(e2.calculate_tax())
    print(e2.total_calculate())
