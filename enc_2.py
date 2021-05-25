class BankAccount:
    def __init__(self, owner, account, balance, password):
        self.owner = owner
        self.account = account
        self.__balance = balance
        self.__password = password

    def balance_check(self, parol):
        if parol == self.__password:
            b = input('На сколько вы хотите изменить свой баланс? ')
            self.__balance += int(b)
            print('Ваш баланс: ' + str(self.__balance) + ' рублей')
        else:
            print('Неверный пароль')


print('Регистрация')
name = input('Введите имя: ')
password = input('Придумайте пароль: ')
egor = BankAccount(name, 666, 0, password)
print()
parol = input('Для того, чтобы пополнить баланс ведите пароль: ')
egor.balance_check(parol)
