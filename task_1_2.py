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

print('Три песни звучат', random_song_1[::][1] + random_song_2[::][1] + random_song_3[::][1] , 'минут') 

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