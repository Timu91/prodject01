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