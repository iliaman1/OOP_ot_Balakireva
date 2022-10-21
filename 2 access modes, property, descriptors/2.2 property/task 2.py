class WindowDlg:
    def __init__(self, title, w, h):
        self.__title = title
        self.__width = w
        self.__height = h

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) == int and 0 <= w <= 10000:
            self.__width = w
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, w):
        if type(w) == int and 0 <= w <= 10000:
            self.__height = w
            self.show()