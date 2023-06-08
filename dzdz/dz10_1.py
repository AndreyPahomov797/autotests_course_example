# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string
def generate_random_name():
    """
                 Генератор выдает два слова случайной длины (до 15 символов), состоящих из случайных букв.
                 """
    letters = string.ascii_lowercase # Записываем в строку алфавит
    while True:  # Бесконечный цикл, чтобы обращаться к следующей итерации
        long_word = random.randint(1, 15) # Любое целое число от 1 до 15, определяющая длину слова
        long_word_2 = random.randint(1, 15)
        word_1 = ''
        word_2 = ''
        for i in range(long_word):  # Пробегает по длине слова
            index = random.randint(0, 25)  # Рассчитывается случайный порядковый номер буквы алфавита
            word_1 += letters[index]
        for i in range(long_word_2):
            index = random.randint(0, 25)
            word_2 += letters[index]
        yield word_1+' '+word_2
gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))