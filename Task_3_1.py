# Task 1

a = float(input('Введите Делимое: '))
b = float(input('Введите Делитель: '))


def delenie(a, b):
    return a / b


if b == 0:
    raise ZeroDivisionError('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ !!!')

print('Ваш ответ: {}'.format(delenie(a, b)))