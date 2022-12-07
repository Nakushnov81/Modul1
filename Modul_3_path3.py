print('Задание 1: ')
from math import sqrt
a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третей стороны: '))
def area(a, b, c):
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'Площадь треугольника равна {s}')
area(a, b, c)