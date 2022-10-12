# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from functools import reduce

my_num = float(input('Введите число: '))
if my_num < 0:
    my_num *= -1
Float_Num_Summ = reduce(lambda a, b: int(a)+int(b),
                        list(filter(lambda x: x != '.', str(my_num))))
print(f'Сумма чисел равна: {Float_Num_Summ}')
