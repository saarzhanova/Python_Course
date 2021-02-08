def season(x):
    if x in [1, 2, 12]:
        x = 'зима'
    elif x in [3, 4, 5]:
        x = 'весна'
    elif x in [6, 7, 8]:
        x = 'лето'
    elif x in [9, 10, 11]:
        x = 'осень'
    else:
        x = 'нет такого месяца'
    return x


s = season(44)
print(s)