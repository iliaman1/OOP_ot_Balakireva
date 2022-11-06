class VideoItem:
    def __init__(self, title: str, descr: str, path: str):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self, rating: int = 0):
        self.__rating = rating

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, val: int):
        if type(val) != int or 5 < val or val < 0:
            raise ValueError('неверное присваиваемое значение')

        self.__rating = val
