class Rect:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return 'width: {width}, height: {height}'.format(width=self.width, height=self.height)


r = Rect(100, 20)
print(r)
print(r.width, r.height, r.area())


class Square(Rect):
    def __init__(self, width):
        super().__init__(width, width)


s = Square(20)
print(s)
print(s.width, s.height, s.area())
