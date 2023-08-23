# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
#print(len(my_favorite_songs))

print (my_favorite_songs[0:14])
print (my_favorite_songs[64:77])
print (my_favorite_songs[16:30])
print (my_favorite_songs[51:62])


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import datetime
import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

random_song_1 = random.choice(my_favorite_songs)
random_song_2 = random.choice(my_favorite_songs)
random_song_3 = random.choice(my_favorite_songs)

print(('Три песни звучат', random_song_1[::][1] + random_song_2[::][1] + random_song_3[::][1] , 'минут')) 

# songs = int(my_favorite_songs[0][1] + my_favorite_songs[1][1] + my_favorite_songs[7][1])
# print(int(('Три песни звучат', random_song_1 + random_song_2 + random_song_3, 'минут')))




# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


rds_1 = random.choice(list(my_favorite_songs_dict.values()))
rds_2 = random.choice(list(my_favorite_songs_dict.values()))
rds_3 = random.choice(list(my_favorite_songs_dict.values()))
print('Три песни звучат',rds_1 + rds_2 + rds_3, 'минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

calendar = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30, 
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}

m = int(input("Номер месяца: "))

if m == 1 in calendar:
    print('Вы ввели Январь.', calendar[m], 'дней')
elif m == 2 in calendar:
    print('Вы ввели Февраль.', calendar[m], 'дней')
elif m == 3 in calendar:
    print('Вы ввели Март.', calendar[m], 'дней')
elif m == 4 in calendar:
    print('Вы ввели Апрель.', calendar[m], 'дней')
elif m == 5 in calendar:
    print('Вы ввели Май.', calendar[m], 'дней')
elif m == 6 in calendar:
    print('Вы ввели Июнь.', calendar[m], 'дней')
elif m == 7 in calendar:
    print('Вы ввели Июль.', calendar[m], 'дней')
elif m == 8 in calendar:
    print('Вы ввели Август.', calendar[m], 'дней')
elif m == 9 in calendar:
    print('Вы ввели Сентябрь.', calendar[m], 'дней')
elif m == 10 in calendar:
    print('Вы ввели Октябрь.', calendar[m], 'дней')
elif m == 11 in calendar:
    print('Вы ввели Ноябрь.', calendar[m], 'дней')
elif m == 12 in calendar:
    print('Вы ввели Декабрь.', calendar[m], 'дней')
else:
    print('Такого месяца нет!')


    #---------------------------------------------------------------------------------------------------------------------------------------------------


    # Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for title, type in titles.items():
    total_quantity = 0
    total_cost = 0
    for titles in store[type]:
        total_quantity += titles['quantity']
        total_cost += titles['price']
    print(title, " - ",total_quantity," шт, ",total_cost * total_quantity," руб")

    