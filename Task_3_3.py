# Task 3

def my_func(a, b, c):
    if (a >= c and b > c) or (a > c and b >= c):
        return a + b
    elif (b >= a and c > a) or (b > a and c >= a):
        return b + c
    elif (c >= b and a > b) or (c > b and a >= b):
        return a + c
    else:
        return f'Наверное все числа одинаковые, в след раз введите другую комбинацию...'


s = input('Введите через пробел три числа: ')
l = s.split()
a = float(l[0])
b = float(l[1])
c = float(l[2])
print(f'Сумма двух наибольших чисел равна: {my_func(a, b, c)}')
