# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты
import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

def test_1():
    assert all_division(1, 2) == 0.5
def test_2():
    assert all_division(4, 2, 2) == 1
def test_3():
    try:
        all_division(1, 0) == 0.5
    except Exception as error:
        print(error)
        assert error == 'division by zero'

test_1()
test_2()
test_3()