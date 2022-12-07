# Модуль 3 часть 2

print('Задание 1: ')
l = [1, 4, 1, 6, 'hello', 5, 'hello']
y = list(set(l))
s=[]
for i in l:
    if i not in y or y.remove(i):
        s.append(i)
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