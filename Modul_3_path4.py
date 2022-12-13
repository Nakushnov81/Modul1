print('Задание 1: ')
import json
# x = {'user': 'user1'}
# with open('register.json', 'w', encoding='utf-8') as file:
#     json.dump(x, file)

def register(login, password):
    with open('register.json', 'r', encoding='utf-8') as file:
        x = json.load(file)
    if login not in x:
        x[login] = password
        with open('register.json', 'w', encoding='utf-8') as file:
            json.dump(x, file)
            print('Сохранен')
    else:
        print('Логин занят')

def input_log(login, password):
    with open('register.json', 'r', encoding='utf-8') as file:
        x = json.load(file)
    if login in x:
        if password == x[login]:
            print('Вход разрешен!')
        else:
             print('Неверный пароль')
    else:
        print('Логин не найден')

while True:
    q1 = input('Если вы хотите войти нажмите i, если зарегистрироваться - r: ')
    if q1 == 'i':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        x = input_log(login, password)
    elif q1 == 'r':
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        x = register(login, password)
    else: break
