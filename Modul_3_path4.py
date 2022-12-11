print('Задание 1: ')
import json
x = {}
q1 = input('Вход или Регистрация')
if q1 == 'вход':
    ...
elif q1 == 'регистрация':
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login not in x:
        register(login, password)


def register(login, password):
    with open('register.json', 'r', encoding='utf-8') as file:
        x = json.load(file)
        if login not in x.keys():
            x[login] = password
            with open('register.json', 'w', encoding='utf-8') as file:
                json.dump(login, file)


        else: print('Логин занят')





def input_log():
