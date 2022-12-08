'''print('Задание 1: ')
from math import sqrt
a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третей стороны: '))
def area(a, b, c):
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c)) # без импорта библиотеки (p*(p-a)*(p-b)*(p-c))**0.5
    print(f'Площадь треугольника равна {s}')
area(a, b, c)

print('Задание 2: ')
s = 'Было просто пасмурно, дуло с севера,\n' \
    'А к обеду насчитал сто градаций серого.\n' \
    'Так всегда первого ноль девятого,\n' \
    'То ли весь мир сошёл с ума, то ли я — того.\n' \
    'На столе записка от неё смятая,\n' \
    'Недопитый виски допиваю с матами.\n' \
    'Посмотрю в окно, допишу главу,\n' \
    'Первое сентября, дворник жжёт листву.\n' \
    'И серым облакам наплевать на нас,\n' \
    'Если знаешь, как жить — живи\n' \
    'Ты хотела плыть, как все?\n' \
    'Так плыви…'
def string(d):
    for i in d.split():
        if len(i) > 5:
            d = d.replace(i, '')
    print(d)
string(s)

# Вариант 2

def string(d):
    p = str()
    for i in d.split():
        if len(i) < 5:
            p += i+' '
    print(p)
string(s)
'''
print('Задание 3: ')

from random import randint
n = int(input('Введите количесво чисел: '))
m = [randint(0, 100) for i in range(n)]
print(m)
s = []
def maxi(d):
    for i in range(0, n):
        if d[i] > 10:
            s.append(d[i]/10)
        else:
            s.append(d[i])
    s.sort(reverse=True)

    print(s)
#def exchange(m):
#    for i in range(0, n):


maxi(m)
'''def maxim(m):
    for i in range(0, len(m)):
        if m[i] > 10:
            m[i] = m[i]/10
            s.append(m[i])
            return s.append(m[i])
    print(s)

maxim(m)'''







