
from random import randint
raw = 3
col = 5
min = 1
max = 10
# Создание списка

def fill_list (col, min, max):
    return [randint(min, max) for i in range(col)]

# Создание двумерного массива из случаных чисел

def fill_matrix(raw, col, min, max):
    return [[randint(min, max) for j in range(col)] for i in range(raw)]
 
# Вывод на печать

print(fill_list (col, min, max))

array = fill_matrix(raw, col, min, max)
print(array)