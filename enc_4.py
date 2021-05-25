class Student:
    def __init__(self, name, willing_hours, homework):
        self.name = name
        self.__will = willing_hours
        self.student = True
        self.homework = homework
        self.deadline = 0

    def set_will(self, will):
        if will in range(1, 8):
            self.__will = will
        else:
            print('Столько нельзя ботать.')

    def get_will(self):
        print(str('Еще ' + str(self.__will) + ' часов ' + self.name + ' готов(a) работать сегодня'))
        return self.__will

    def __kick_out(self):
        self.student = False
        print('Студента ' + self.name +' исключили из университета')

    def _do_homework(self):
        if self.student is True:
            if self.homework > 0:
                if self.__will > 0:
                    print(self.name + ' выполнил(a) 1 домашнее задание из ' + str(self.homework))
                    self.homework -= 1
                    self.__will -= 1
                else:
                    print('Студент ' + self.name + ' слишком устал. Доделает завтра')
                    self.sleep()
            else:
                print(self.name + ' сделал(a) все задания и может отдыхать')
                if self.deadline > 0:
                    self.deadline -= 1
        else:
            print('Зачем? ' + self.name + ' не студент.')

    def sleep(self):
        if self.student is True:
            if self.homework > 0:
                if input('У вас завтра ' + str(self.homework) + ' дедлайнов, вы точно хотите лечь спать? ') == 'yes':
                    print(self.name + ' спит.')
                    self.deadline = self.homework
                    self.set_will(int(input('Сколько завтра хотите ботать?')))
                    self.get_will()
                    if self.deadline > 3:
                        self.__kick_out()
                else:
                    self.__will += 1
                    self.set_will(self.__will)
                    self.get_will()
            else:
                print(self.name + ' спокойно спит.')
                self.set_will(int(input('Сколько завтра хотите ботать?')))
                self.get_will()
        else:
            print(self.name + ' не студент. Общаги нет - негде спать.')


eugene = Student('Евгений', 3, 4)
eugene.get_will()
eugene._do_homework()
eugene._do_homework()
eugene.get_will()
eugene._do_homework()
eugene._do_homework()   # Здесь студент Евгений устал и захотел ленчь спать.
# Если напечатать "yes", то он ляжет спать и пропустит дедлайн.
# Если напечатать, например, "no", то Евгений найдет в себе силы соделать ещё одно задание.

print()
sergey = Student('Сергей', 4, 1)
sergey.get_will()
sergey._do_homework()
sergey._do_homework()   # У студента Сергея было мало домашней работы.
print()
nikolay = Student('Николай', 1, 6)  # Студент Николай - бездельник. Он не любит учиться.
nikolay.get_will()
nikolay._do_homework()
nikolay._do_homework()
# Если Николай не найдет в себе силы продержаться ещё хотя бы 2 часа и сделать 2 задания,
# исключение неизбежно.
nikolay._do_homework()
nikolay.sleep()