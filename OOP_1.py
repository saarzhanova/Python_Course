class Person:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def introduce(self):
        print(self.name + ' has got ' + str(self.money) + ' dollars now')
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

    def __init__(self, money, tool):
        self.money = money
        self.tool = tool

    def needs(self):
        print('A person with a ' + self.tool + ' needs ' + str(self.money) + ' dollars')
        return self.money, self.tool

    def rob(self, somebody):
        if somebody.money > self.money:
            somebody.money -= self.money
            print('A person with a ' + self.tool + ' stole ' + str(self.money) + " dollars from " + somebody.name)
            self.money = 0
        else:
            self.money -= somebody.money
            somebody.money = 0
            print('A person with a ' + self.tool + ' stole all the money from ' + somebody.name)
        return somebody.introduce(), self.needs()


Mike = Person('Mike', 100)
Lisa = Person('Lisa', 400)
Luke = Robber(300, 'gun')
Mike.introduce()
Lisa.introduce()
Luke.needs()
print()
Luke.rob(Mike)
print()
Luke.rob(Lisa)
