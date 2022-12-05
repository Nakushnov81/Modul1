#Модуль 3.1
print('Уровень 1:')
x = int(input('Введите сумму вклада: '))
y = int(input('Введите сумму которую хотите забрать: '))
p = int(input('Введите процент: '))
year = 0
while x < y:
    year+=1
    x += x*p//100
else:
    print(f'Надо подождать {year} лет')
    print(f'Будет накоплено {x} рублей')

print('Уровень 2:')
n = int(input('Введите кол-во повторений: '))
s = 0
while s < n:
    s+=1
    print('for - частный случай цикла while')

print('Уровень 3: ')

num1 = int(input('Введите число: '))

s = 0

while num1 > 0:
    s = s + num1%10
    num1 = num1//10
print(f'Сумма цифр числа {num1} равна {s}')
