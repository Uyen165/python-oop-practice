class Dataset:
    def __init__(self, name, sample_count):
        self.name = name
        self.sample_count = sample_count

    @property
    def sample_count(self):
        return self._sample_count

    @sample_count.setter
    def sample_count(self, new_sample_count):
        if new_sample_count > 0:
            self._sample_count = new_sample_count
        else:
            raise ValueError ("Loi: So luong dong phai > 0")

    def __repr__(self):
        return f"Dataset(name= '{self.name}', sample_count= {self.sample_count})"

if __name__ == '__main__':
    dt1 = Dataset("Tu Uyen", 10)
    dt2 = Dataset("TU", 20)
    print(dt1)
    print(dt2)