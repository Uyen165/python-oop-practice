class OnlineCourse:
    MAX_STUDENT = 100

    def __init__(self, title, tuition):
        self.title = title
        self.tuition = tuition

    @property
    def tuition(self):
        return self._tuition
    @tuition.setter
    def tuition(self, new_tuition):
        if new_tuition < 0:
            raise ValueError("Hoc phi khong duoc am")
        else:
            self._tuition = new_tuition

    def apply_scholarship(self, percent):
        if 0 < percent <= 100:
            self._scholarship_rate = percent / 100
        else:
            raise ValueError("Ty le hoc bong phai tu 0 - 100")

    def get_final_tuition(self):
        if hasattr(self, "_scholarship_rate"):
            return self.tuition * (1 - self._scholarship_rate)
        else:
            return self.tuition

    def __repr__(self):
        return f"OnlineCourse(title='{self.title}', tuition={self.tuition})"

if __name__ == '__main__':
    kh1 = OnlineCourse("Khoa hoc DS", 100)
    print(kh1)
    print(kh1.tuition)
    kh1.apply_scholarship(20)
    print(kh1.get_final_tuition())