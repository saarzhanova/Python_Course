class figure:

    def __init__(self):
        self.color = 'серый'

    def change_color(self, new):
        self.color = new
        print('Поменяли цвет фигуры!')
        self.check()

    def check(self):
        pass


class oval(figure):

    def __init__(self, a, b):
        super().__init__()
        self.x = a
        self.y = b

    def check(self):
        print('Представьте ' + self.color + ' овал с малой полуосью - ' + str(self.x) + ', и большой полуосью - ' + str(self.y))


class square(figure):

    def __init__(self, a):
        super().__init__()
        self.a = a

    def check(self):
        print('Представьте ' + self.color + ' квадрат со стороной ' + str(self.a))


Oval = oval(1, 2)
Square = square(2)
Oval.check()
Square.check()
print()
Square.change_color('розовый')
Oval.change_color('желтый')
