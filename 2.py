x = [1, 1, 2, 5, 23, 4, 23, 1]
a = []
for i in x:
    if x.count(i) >= 2 and i not in a:
        a.append(i)
    else:
        None
for item in a:
    print('"' + str(item) + '"' + ' встречается в списке ' +str(x.count(item)) + ' раз(а)')