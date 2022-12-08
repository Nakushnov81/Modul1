# Модуль 3 часть 2

print('Задание 1: ')
l = [1, 4, 1, 6, 'hello', 5, 'hello']
s = []
for i in range(0, len(l)):
    for j in range(0, len(l)):
        if i != j and l[i] == l[j] and l[i] not in s:
            s.append(l[i])
print(s)

print('Задание 2: ')
from random import randint
n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
s = 0
for x in m:
    for y in x:
        if y > s:
            s = y  # /Можно ли написать этот код в одну строчку?
print(m)
print(s)

print('Задание 3: ')
eng = {
    'рука': 'hand',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer'
}
k = list(eng.values())
v = list(eng.keys())

rus = dict(zip(k, v))
print(rus)
