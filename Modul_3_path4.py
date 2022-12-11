print('Задание 1: ')
import json
x = {}


def register(login, password):
    with open('register.json', 'r', encoding='utf-8') as file:
        x = json.load(file)
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if login not in x.keys():
            x[login] = password
            with open('register.json', 'w', encoding='utf-8') as file:
                json.dump(login, file)
        else: print('Логин занят')

def input_log():
    with open('register.json', 'r', encoding='utf-8') as file:
        x = json.load(file)
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        if login in x:
            if password == x[login]:
                print('Вход разрешен!')
            else:
                print('Неверный пароль')
        else:
            print('Логин не найден')


while True:
    q1 = input('Вход или Регистрация')
    if q1 == 'вход':
        input_log()

    elif q1 == 'регистрация':
        register()
    #else:
        #break
