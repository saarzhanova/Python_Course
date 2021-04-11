import time

s = time.process_time()
a = ' овца'
b = ' овцы'
c = ' овец'
print('Считаем овец!')
for i in range(100001):
    if len(str(i)) > 1 and str(i)[-2]+str(i)[-1] in ['11', '12', '13', '14']:
        print(str(i) + c)
    elif str(i)[-1] == '1':
        print(str(i) + a)
    elif str(i)[-1] in ['2', '3', '4']:
        print(str(i) + b)
    else:
        print(str(i) + c)
f = time.process_time()
now = time.strftime('%d.%m.%Y.%H.%M.%S')
file = open(f'{now}.txt', 'w', encoding='utf-8')
file.write("Время, за которое программа считает 100001 овцу: " + str(f-s) + " секунд")
file.close()
