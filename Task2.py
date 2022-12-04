x = int(input('Введите сумму вклада: '))
y = int(input('Введите сумму которую хотите забрать: '))
p = int(input('Введите процент: '))


year = 0

while x < y:
    year+=1
    x += x*p//100
else:
    print(year)
    print(x)


