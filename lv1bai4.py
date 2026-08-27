class Movie:
    MIN_RATING = 0.0
    MAX_RATING = 10.0

    def __init__(self, title:str, director:str, duration:int):
        self.title = title
        self.director = director
        if duration <= 0:
            raise ValueError("Thời lượng phim phải lớn hơn 0 phút")
        self._duration = duration
    @property
    def duration(self):
        return self._duration

    def rate_movie(self, score):
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            raise TypeError("Điểm số phải là dạng số!")
        if score < Movie.MIN_RATING or score > Movie.MAX_RATING:
            raise ValueError("Điểm số phải từ 0.0 đến 10.0!")
        self._rating = score

    def get_rating(self):
        if hasattr(self, "_rating"):
            return self._rating
        else:
            return f"Chưa có đánh giá!"
    #def get_rating(self):
    #return getattr(self, "_rating", "Chưa có đánh giá!")

    def __repr__(self):
        return f"Movie(title='{self.title}', director='{self.director}', duration={self.duration})"
if __name__ == '__main__':
    m1 = Movie("Hoang tu be", "Noi dung", 90)
    print(m1)
    m1.rate_movie(8.8)
    print(m1.get_rating())
    m2 = Movie("Kieu hanh va Dinh kien", "Noi dung", 120)
    print(m2.get_rating())
