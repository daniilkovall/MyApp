import math


# Функция для нахождения корней квадратного уравнения
def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Корней нет.')
    elif d == 0:
        x = -b / (2 * a)
        print(' Есть один корень:', x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(' Два корня:', x1, 'and', x2)


a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

quadratic(a, b, c)