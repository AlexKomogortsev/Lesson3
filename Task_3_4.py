# Task 4_1

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))


def my_func(x, y):
    return x ** y


print(f'Ваш ответ: {my_func(x, y)}')

# Task 4_2

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))


def my_func(x, y):
    b = 1
    a = 1
    while a <= abs(y):
        b = b / x
        a += 1
    return b


print(f'Ваш ответ: {my_func(x, y)}')
