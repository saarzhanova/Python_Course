class Ticket:
    def __init__(self, price):
        self.price = price
        self.benefitial = price/3


class Passenger:
    def __init__(self, money, benefits):
        self.money = int(money)
        self.tickets = 0
        self.benefits = benefits

    def wants_to_buy(self, ticket, amount, destination):
        if self.benefits == 'Yes':
            price = ticket.benefitial
        else:
            price = ticket.price
        if int(self.money) >= int(price) * int(amount):
            self.money -= int(price)
            self.tickets += int(amount)
            print('You have purchased', amount, 'ticket(s) to', destination)
            print('Now you have', self.tickets, 'ticket(s)')
        else:
            print("You don't have enough money")
            print('Your amount of money:', self.money)
            print('The ticket(s) price is', int(price) * int(amount))
            print('You have', self.tickets, 'ticket(s) to', destination)


ticket = Ticket(120)
money = input('Put money in your account: ')
benefits = input('Are you a student or a retiree? ')
Mike = Passenger(money, benefits)
print()
while True:
    answer = input('Would you like to buy a ticket? ')
    if answer == "Yes":
        destination = input('Where would you like to go? ')
        Mike.wants_to_buy(ticket, input('How many tickets would you like to purchase? '), destination)
    else:
        print('Thank you for time!')
        exit()




