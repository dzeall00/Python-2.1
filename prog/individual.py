# Треугольник задан координатами своих вершин. Найти периметр и площадь треугольника. 

import math

# ввод координат вершин треугольника
print('Enter the coordinates of the vertex A: ')
x1, y1 = map(float, input().split())
print('Enter the coordinates of the vertex B: ')
x2, y2 = map(float, input().split())
print('Enter the coordinates of the vertex C: ')
x3, y3 = map(float, input().split())

# вычисление длин сторон треугольника
AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
AC = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
p = (AB + AC + BC)  # Периметр треугольника ABC

print('')
print('Perimeter = {:.2f}'.format(p))  # Выводим периметр
p = p / 2  # полупериметр
# Площадь треугольника ABC
S = math.sqrt(p * (p - AB) * (p - AC) * (p - BC))
print('Square = {:.2f}'.format(S))
