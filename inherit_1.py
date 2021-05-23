class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)

    def howplaces(self, s):
        pass


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Worker(Table):
    def work(self, hours):
        money = hours * 25
        if hours >= 4:
            print("You earned", money, "$")
        else:
            print("Don't get up of the table! You are not done yet")
        self.trash_check(hours)
        return money

    def trash_check(self, hours):
        surface = hours * 1.5
        if self.width * self.long >= surface > (self.width * self.long)/2:
            print("Maybe you should clean your table up! Or you will get fired")
        elif surface >= self.width * self.long:
            print('you are a pig')
            if input('Do you want to clean your table?') == 'yes':
                surface = 0
                print('You have cleaned your table! Get back to work!')
            else:
                print('you are fired!')
                exit(5)
        return surface


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()

t_2 = Table(1, 3, 0.7)
t_2.outing()
t_2.howplaces(8)

w_1 = Worker(2, 3, 6)
while True:
    h = input('Input working hours: ')
    if h == 'no':
        exit()
    else:
        w_1.work(int(h))
