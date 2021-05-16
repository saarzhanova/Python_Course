class Krug:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


class Kvadrat:
    def __init__(self, height, color):
        self.height = height
        self.color = color


class Treugolnik:
    def __init__(self, height, color):
        self.height = height
        self.color = color

class Box:
    def __init__(self):
        self.figures = []

    def add(self, something):
        self.figures.append(something)

    def check(self):
        inthebox = []
        for el in self.figures:
            if isinstance(el, Krug):
                inthebox.append('krug')
            elif isinstance(el, Kvadrat):
                inthebox.append('kvadrat')
            elif isinstance(el, Treugolnik):
                inthebox.append('treugolnik')
        print(inthebox)
        return(inthebox)


figura = Krug(10, 'red')
eshe_firura = Kvadrat(15, 'blue')
poslednyaya_fiura = Treugolnik(5, 'yellow')

box = Box()
box.add(figura)
box.check()
print()
box.add(eshe_firura)
box.add(figura)
box.add(figura)
box.check()

