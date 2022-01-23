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
