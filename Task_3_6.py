# Task 6_1
#
# def int_func(s):
#     return s.capitalize()
#
# print(int_func(input('Введите слово из маленьких латинских букв: ')))
#
# Task 6_2

def int_func(s):
    return s.capitalize()


s1 = input('Введите строку из слов, разделенных пробелами и состоящих из маленьких латинских букв: ')
s2 = ''
l = s1.split()
for x in l:
    int_func(x)
    s2 += int_func(x) + ' '
print(s2)
