class DataSequence:
    def __init__(self, ds_so):
        if not isinstance(ds_so, (list, tuple)):
            raise TypeError("Vui lòng nhập một danh sách")
        for x in ds_so:
            if isinstance(x, bool) or not isinstance(x, (int, float)):
                raise ValueError("Tất cả các phần tử trong danh sách phải là số")

        self.ds_so = list(ds_so)

    def __len__(self):
        return len(self.ds_so)

    #Thắc mắc 1: Tại sao lại cần hàm này? Trong khi bình thường có thể truy cập trực tiếp index mà đâu cần hàm? (Note gthich bên dưới)
    def __getitem__(self, index):
        return self.ds_so[index]

    #Thắc mắc 2: Kiến thức về hàm __call__ (Note dưới ghi chú)
    #Điểm quan trọng: Đây là một phương thức đặc biệt cho phép thực hiện hành động khi đối tượng được gọi
    def __call__(self, scale_factor):
        if not isinstance(scale_factor, (int, float)) or isinstance(scale_factor, bool):
            raise TypeError("Hệ số tỉ lệ phải là một số")
        #Nhân từng phần tử với scale_factor
        new_data = [x * scale_factor for x in self.ds_so]
        return DataSequence(new_data)

    def __repr__(self):
        return f"DataSequence({self.ds_so})"

if __name__ == '__main__':
    list_one = DataSequence([1, 2, 3, 4, 5])
    print(list_one)
    print(len(list_one))
    print(list_one[0]) #Nhờ hàm __getitem__ mới truy cập kiểu này được, không thì sẽ lỗi
    n_dt = list_one(3) #Lợi ích của hàm __call__, ta chỉ cần gọi đối tượng và truyền tham số tương tự vs hàm
    print(n_dt)  