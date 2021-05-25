class Figures:
    def __init__(self, color, shape, size):
        self.color = color
        self._shape = shape
        self.__size = size


f = Figures('yellow', 'kvadrat', 'small')
print(f.color)
print(f._shape)
print(f.__size)
