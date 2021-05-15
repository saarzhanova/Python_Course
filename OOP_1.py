class Person:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def introduce(self):
        print(self.name + ' has got ' + str(self.money) + ' dollars')
        return self.name, self.money

    def share(self, somebody, money):
        if self.money/2 > money:
            self.money -= money
            somebody.money += money
            print(self.name + ' lent ' + somebody.name, str(money) + " dollars. Now " + self.name + "'s got " + str(self.money) + ' and ' + somebody.name + "'s got " + str(somebody.money) + " dollars")
        else:
            print(somebody.name, 'asked', self.name, 'for', str(money),'dollars, but', self.name, 'cold not lend that much')
        return self.money, somebody.money


class Robber:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def introduce(self):
        print(self.name + ' has got ' + str(self.money) + ' dollars')
        return self.name, self.money

    def rob(self, somebody):
        self.money += somebody.money
        somebody.money = 0
        print('Someone stole all ' + somebody.name + "'s money. Now " + self.name + "'s got " + str(self.money) + ' and ' + somebody.name + "'s got nothing. (" + str(somebody.money) + " dollars)")
        return somebody.money


Mike = Person('Mike', 100)
Lisa = Person('Lisa', 300)
Luke = Robber('Luke', 15)
Mike.introduce()
Luke.introduce()
Lisa.introduce()
Luke.rob(Mike)
Lisa.share(Mike, 100)
Lisa.share(Mike, 100)
Lisa.introduce()


