# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Было:
# def getDay(numDay):
#     return {
#         numDay in range(1, 6): 'рабочий день',
#         numDay in range(6, 8): 'выходной день'
#     }[True]


# day = int(input('Введите день недели: '))
# if 1 <= day <= 7:
#     print(f'Это {getDay(day)}')
# else:
#     print('Введен не корректный день недели')

# Стало:
my_day = int(input('Введите день недели: '))
if my_day in range(1, 8):
    num_Day = (lambda day: 'рабочий день' if day in range(
        1, 6) else 'выходной день')(my_day)
    print(f'Это {num_Day}')
else:
    print('Введен не корректный день недели')
