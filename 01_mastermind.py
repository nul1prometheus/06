# -*- coding: utf-8 -*-
import random
# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля).

def randomizing():
    global komp_number
    komp_number = random.randint(0, 9)
    return komp_number

komp_number_all = []

for _ in range(4):
    while randomizing() in komp_number_all:
        randomizing()
    komp_number_all.append(komp_number)
# print(komp_number_all)
# Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# user_digit = None
# def input_digit():
#     user_digit = input()
#     # try:
#     #     int(user_digit)
#     # except ValueError:
#     #     print('Digit require, try again')
#     # while (int(user_digit) / 10) > 1:
#     #     print('Input 1 digit! Try again')
#     #     user_digit = input()
#         # try:
#         #     int(user_digit)
#         # except ValueError:
#         #     print('Digit require, try again')
#     return user_digit

user_number_list = []

# for _ in range(4):
#     print('Input', _, 'digit:')
#     user_digit = input()
#     # print('Require different digits, try again')
#         # user_number_list.clear()
#     user_number_list.append(int(user_digit))
#     print(user_number_list)
# print(user_number_list)
# user_number = input()
# user_number_int = int(user_number)
# while (user_number_int < 1000):
#     print('Need 4 digits! Try again please')
#     user_number = input()
#     user_number_int = int(user_number)
# if (user_number[0] == user_number[1]) or (user_number[0] == user_number[2]) or (user_number[0] == user_number[3]):
#     print('Every digits must be different! Try again')
#     user_number = input()
#     user_number_int = int(user_number)
# if (user_number[1] == user_number[2]) or (user_number[1] == user_number[3]):
#     print('Every digits must be different! Try again')
#     user_number = input()
#     user_number_int = int(user_number)
# if user_number[2] == user_number[3]:
#     print('Every digits must be different! Try again')
#     user_number = input()
#     user_number_int = int(user_number)
# print(user_number)
#
cows = 0
bulls = 0
moves = 0
while bulls < 4:
    cows = 0
    bulls = 0
    user_number = input()
    user_number_int = int(user_number)
    forwhilenumber = user_number_int
    user_number_list.clear()
    while forwhilenumber >0:
        user_number_list.append(forwhilenumber % 10)
        forwhilenumber //= 10

    user_number_list.reverse()
    # print(user_number_list)
#
# # компьютер сообщают о количестве «быков» и «коров» в названном числе
# # «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
# #       что и в задуманном числе
# # «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
# #       что и в задуманном числе

    for _ in range(4):
        if (user_number_list[_] == komp_number_all[_]):
            bulls += 1
    for _ in range(4):
        for __ in range(4):
            if user_number_list[_] == komp_number_all[__]:
                cows += 1
    print('bulls =', bulls)
    print('cows =', cows)
    moves += 1
print('Moves:', moves)
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

