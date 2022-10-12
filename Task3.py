# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Было:
# import math


# def abDistance2D(a, b):
#     return round(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 2)


# print('Введите координаты точки А (X, Y) через пробел:')
# А = list(map(int, input().split(' ')))
# print('Введите координаты точки B (X, Y) через пробел:')
# B = list(map(int, input().split(' ')))
# print(f'Расстояние между точками A и B: {abDistance2D(А, B)}')

# Стало:
from math import sqrt


print('Введите координаты точки А (X, Y) через пробел:')
Point_А = list(map(int, input().split(' ')))
print('Введите координаты точки B (X, Y) через пробел:')
Point_B = list(map(int, input().split(' ')))
ab_Distance_2D = (lambda a, b: round(
    sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 2))(Point_А, Point_B)
print(f'Расстояние между точками A и B: {ab_Distance_2D}')
