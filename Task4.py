# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Было:
# def getFloatNumSumm(num):
#     summ = 0
#     for i in str(num):
#         if i != '.':
#             summ += int(i)
#     return summ


# num = float(input('Введите число: '))
# if num < 0:
#     num *= -1

# print(f'Сумма чисел равна: {getFloatNumSumm(num)}')

# Стало:
from functools import reduce

my_num = float(input('Введите число: '))
if my_num < 0:
    my_num *= -1
Float_Num_Summ = reduce(lambda a, b: int(a)+int(b),
                        list(filter(lambda x: x != '.', str(my_num))))
print(f'Сумма чисел равна: {Float_Num_Summ}')
