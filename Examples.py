# Генерация списка из случайных чисел
from random import randint

numbers = []
for i in range(3):
    numbers.append(randint(-10, 10))
print(numbers)

lst = [randint(-10, 10) for i in range(10)]
print(lst)

#
a = [3, 4, 5]
b = [1, 2, 3]
c = [(x-y)**2 for x, y in zip(a, b)]  # сложить эемементы списка
print(c)

import math
def jj(c):
    total = 0
    for i in c:
        total += i
    d = math.sqrt(total)
    return d


print (round(jj(c),3))


# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
import random
import os

def ParsIntToList(a):  # Разбирает число на список
    numbers = []
    while a > 0:
        numbers.append(a % 10)
        a //= 10
    numbers.reverse()
    return numbers

def MaxInList(list):  # Возвращает максимальное число в списке
    max = list[0]
    for i in list:
        if i > max: max = i
    return max

n = random.randint(10, 99)
os.system('cls')
print(f'N = {n}')
print(f'{MaxInList(ParsIntToList(n))} является максимальной цифрой числа')
