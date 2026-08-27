class StudentProfile:
    GRADUATION_SCORE = 5.0

    def __init__(self, student_id:str, full_name:str):
        self.student_id = student_id
        self.full_name = full_name

    @property
    def gpa(self):
        return getattr(self, "_gpa", None)

    def add_gpa(self, gpa):
        if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
            raise TypeError("GPA phải là số!")
        if gpa < 0.0 or gpa > 10.0:
            #ValueError là lỗi xảy ra khi hàm nhận đúng kiểu dữ liệu nhưng giá trị của dữ liệu đó lại sai quy tắc tính toán hoặc xử lý của hàm
            raise ValueError("GPA phải nằm trong khoảng 0.0 - 10.0!")
        self._gpa = gpa

    def is_eligible_to_graduate(self):
        if hasattr(self, "_gpa"):
            if self._gpa >= self.GRADUATION_SCORE:
                return True
            else:
                return False
        else:
            #RuntimeError là lỗi khi ctrinh đang thực thi nhưng không thể tiếp tục do một tình huống không hợp lệ/Python không biết phải xử lý ra sao
            raise RuntimeError("Sinh viên chưa có điểm GPA để xét tốt nghiệp")

    @classmethod
    def from_csv_line(cls, csv_line:str):
        infor = csv_line.split(",")
        student_id = infor[0]
        full_name = infor[1]
        #Hoặc: student_id, full_name = csv_line.split(',')
        return cls(student_id.strip(), full_name.strip())

    @staticmethod
    def classify_gpa(gpa):
        if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
            raise TypeError("GPA phải là số!")
        if gpa < 0.0 or gpa > 10.0:
            raise ValueError("GPA phải nằm trong khoảng 0.0 - 10.0!")
        if gpa >= 8.0:
            return f"Giỏi"
        elif gpa >= 6.5:
            return f"Khá"
        elif gpa >= 5.0:
            return f"Trung bình"
        else:
            return f"Yếu"

    def __repr__(self):
        return f"StudentProfile(student_id='{self.student_id}', full_name='{self.full_name}')"

if __name__ == '__main__':
    s1 = StudentProfile("24103100165", "Nguyễn Tú Uyên")
    print(s1)
    kq = StudentProfile.classify_gpa(9.0)
    print(kq)
    print(s1.gpa) #None
    s1.add_gpa(8.8)
    print(s1.is_eligible_to_graduate()) #True
    s2 = StudentProfile.from_csv_line("  24103100130, Kim Viet Anh  ")
    print(s2) #StudentProfile(student_id='24103100130', full_name='Kim Viet Anh')
        