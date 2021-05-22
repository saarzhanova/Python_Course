class Dela:
    # Класс для заданий, которые менеджер дает своим работникам
    def __init__(self, delo, level):
        self.delo = delo
        self.level = level


class Rabochii:
    # Класс рабочих.
    # У них есть имя, им платят зарплату, у них есть силы, чтобы работать, мэнэджер, список дел и предупреждения.
    def __init__(self, name, salary, stamina, manager=None):
        self.name = name
        self.salary = salary
        self.stamina = stamina
        self.manager = manager
        self.dela = []
        self.strike = 0

    def check(self):
        # Здесь выводится основная информация о работнике
        if self.manager is None: # В случае если у него нет работодателя (менеджира)
            print(self.name + ' ни на кого не работает')
        else:   # В случае если есть
            print(self.name + ' простой рабоч(ий/ая) с зарплатой равной ' + str(self.salary) + '$, количеством страйков равным ' + str(self.strike))
            print(self.name + ' работает на менежира с именем ' + self.manager + ' - не жалуется.')
            print('У рабочего ' + self.name, str(self.stamina) + ' сил')
            i = input('Показать список его дел?')
            if i == 'да' or i == 'yes':
                return self.check_dela()
            else:
                print('Ну, если понадобится, спросите.')

    def check_dela(self):   # Можно посмотреть список дел
        print('У ' + self.name, str(len(self.dela)) + ' дел:')
        for i in range(len(self.dela)):
            print(str(i+1) + ') ' + self.dela[i].delo)

    def do_delo(self):  # "Рабочие" выпоняют дела.
        if len(self.dela) > 0:  # Проверяем наличие дел в списке
            print('Какое дело выполнит ' + self.name + '?')
            for i in range(len(self.dela)):
                print(str(i + 1) + ') ' + self.dela[i].delo)
            n = int(input('Назови цифру')) - 1
            if self.dela[n].level <= self.stamina:  # "Рабочий" выполняет дела, если у него хватает сил.
                print(self.dela[n].delo + ' - выполнено!')
                self.stamina -= self.dela[n].level  # Силы тратятся на выполнение дел.
                print('У рабочего ' + self.name, str(self.stamina) + ' сил осталось')
                self.dela.pop(n)
            else:
                print('не хватает сил выполнить это задание')
        else:
            print('У ' + self.name + 'нет дел')
        return self.dela, self.check_dela()

    def rest(self, hour):   # Чтобы накопить силы - нужно отдохнуть.
        print(self.name + ' присел(а) отдохнуть на ' + str(hour) + ' час(-/а/ов)')
        self.stamina += hour    # Каждый час - плюс 1 к силе
        print('Теперь у него ' + str(self.stamina) + ' сил')


class Manager(Rabochii):
    # Класс менеджира. Он не устает, он сам себе работодатель, у него нет списка дел - он делает то, что считает нужным.
    def __init__(self, name, salary, ):
        super().__init__(self, name, salary)
        self.rabochie = []
        self.name = name
        self.salary = salary

    def check(self):    # Здесь можно узнать главную информацию о менеджире
        print(self.name + ' - успешн(ый/ая) менежер с зарплатой равной ' + str(self.salary) + '$ и количеством подчиненных простых рабочих равным ' + str(len(self.rabochie)))

    def rab_check(self):    # Здесь можно увидеть список его "рабочих"
        print('На менежера ' + self.name + ' работают: ')
        for i in range(len(self.rabochie)):
            print(str(i+1) + ') ' + self.rabochie[i].name)

    def hire(self, name, salary):   # Менеджер может нанять "рабочего".
        if salary > name.salary:    # Для этого нужно предложить ему достаточно зарплату, которая устроит "рабочего".
            name.salary = salary    # Ожидаемая зарплата теперьменяется на ту, которую обещал менеджер.
            self.rabochie.append(name)  # "Рабочий" добавляется в список рабочих менеджире
            print(self.name + ' нанял(а) рабочего с именем ' + name.name)
            name.manager = self.name    # У "рабочего" появляется менеджер.
        else:
            print(name.name + ' не идет работать на ' + self.name + '. Не выгодно.')
        return self.rabochie, self.rab_check()

    def fire(self, name):   # Менеджер может уволить своего "рабочего".
        if name in self.rabochie:
            name.manager = None # У рабочего больше нет работодателя - он безработный.
            i = self.rabochie.index(name)
            self.rabochie.pop(i)
            print(self.name + ' уволил(а) рабочего ' + name.name)
            return name.manager

    def give_strike(self, name):    # Менеджер может давать предупреждения.
        if name in self.rabochie:
            if name.strike < 2:     # Менеджер не любит повторять много раз. Третье предупреждение - увольнение.
                name.strike = int(name.strike) + 1
                print(name.name + ' получил(а) предупреждение от менежира ' + self.name)
            else:
                print('У работника ' + name.name + ' слишком много предупреждений.')
                return self.fire(name)

    def give_delo(self, name, delo, level): # Менеджер может давать своим рабочим поручения разного уровня сложности.
        if name in self.rabochie:
            print(self.name + ' дал(а)  новое задание рабочему ' + name.name)
            name.dela.append(Dela(delo, level))
            return name.check_dela()

# Создание людей с именем, запросами на зарплату и силой.
dima = Rabochii('Дима', 100, 10)
igor = Rabochii('Игорь', 150, 7)
grisha = Rabochii('Гриша', 50, 5)

# Создаем менеджира.
artem = Manager('Артем', 500)

# проверяем, что люди безработные.
dima.check()
artem.check()
print()
# Менеджер нанимает раочих.
artem.hire(dima, 150)
artem.hire(grisha, 100)
artem.hire(igor, 200)
print()
dima.check() # Смотрим информацию о рабочем.
print()
artem.give_strike(grisha)   # Гриша провинился
artem.give_strike(grisha)
artem.give_strike(grisha)   # Здесь гриша уже уволен
grisha.check()  # Убеждаемся в этом
print()
artem.give_delo(dima, 'перебрать документы', 5) # Менеджер дает задания Диме
artem.give_delo(dima, 'сходить за кофе', 12)
print()
dima.do_delo()  # Дима начинает выполнять деля
dima.rest(4)    # Дима отдыхает
dima.rest(4)
dima.do_delo()  # Снова за работу
dima.check()    # Убеждаемся, что дима выполнил все дела

# Я бы ещё хотела добавить возможность рабочим самим уволиться, но на это нужно будет ещё время.

