#Модуль 1
value = (7*5/8+5)/(3 ** 5)
print(value)
#Уровень 2

v = int(input('Введите скорость: '))
t = int(input('Введите время: '))
s = v * t % 109
print('Вася далеко не уехал, всего-то на', s, 'км.')


#Уровень 3
num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
num3 = (num1>num2)*num1 + (num2>=num1)*num2
print(num3)

#Модуль 2
print('Задание 1')
a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)

print('Задание 2')
print('Введите 4 координаты двух фигур от 1 до 8: ')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 in range(1, 9) and x2 in range(1, 9) and y1 in range(1, 9) and y2 in range(1, 9):
    if x1 == x2 or y1 == y2:
        print('YES')
    else:
        print('NO')
else:
    print('Координаты не верны')

print('Задание 3')

x = str(input('Введите пароль: '))
while x.islower() or x.isupper() or len(x) < 8:
    print('Пароль неверен. Введите другой пароль: ')
    x = str(input())
print('Пароль сохранён')
