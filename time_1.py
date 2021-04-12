import time

while True:
    x = int(input('Введите число: '))
    if x >= 0:
        time.sleep(x)
    else:
        exit()