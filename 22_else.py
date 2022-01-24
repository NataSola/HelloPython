# 22. Найти расстояние между точками в пространстве 2D/3D

from random import randint
import math

num_plan = 2    # количество осей координат


def Get_coordinates(num_plan):
    coords = []
    for i in range(num_plan):
        coords.append(randint(-10, 10))
    return coords


def Find_distance(a, b):
    # список элементов (x-y)**2 для каждой пары координат
    elemet_sqrt = [(x-y) for x, y in zip(a, b)]
    total_sum = 0
    for c in elemet_sqrt:
        total_sum += c**2  # сумма квадратов разностей координат
    return round(math.sqrt(total_sum), 3)


point_A = Get_coordinates(num_plan)
point_B = Get_coordinates(num_plan)
print(f'A {point_A}, B {point_B}')
dist = Find_distance(point_A, point_B)
print(f'Расстояние между точками: {dist}')