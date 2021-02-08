x = "топот"
a = []
for i in str(x):
    a.append(i)
a.reverse()
if ''.join(a) == x:
    print('Слово ' + '"' + str(x) + '"' + ' является палиндромом')
else:
    print("Данное слово не является палиндромом")
