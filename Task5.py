# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Было:
# def getSequence(num):
#     sequenceList = []
#     for i in range(1, num+1):
#         sequenceList.append(round((1 + 1 / i)**i, 2))
#     return sequenceList


# def getSequenceSum(sequenceList):
#     sum = 0.0
#     for i in range(0, len(sequenceList)):
#         sum += sequenceList[i]
#     return sum


# num = int(input('Введите число: '))
# if num < 1:
#     print('Число должно быть больше 0')
# else:
#     sequenceList = getSequence(num)
#     print(f'Список из {num} чисел: {sequenceList}')
#     print(f'Сумма чисел: {round(getSequenceSum(sequenceList),2)}')

# Стало:
my_num = int(input('Введите число: '))
if my_num < 1:
    print('Число должно быть больше 0')
else:
    sequence_list = list(
        map(lambda i: round((1 + 1 / i)**i, 2), list(range(1, my_num+1))))
    print(f'Список из {my_num} чисел: {sequence_list}')
    print(f'Сумма чисел: {round(sum(sequence_list), 2)}')
