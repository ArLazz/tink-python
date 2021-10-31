# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел, которая не содержит инструкции if,
# а использует стандартную функцию min. Считайте четыре целых числа и выведите их минимум.

def min4(a, b, c, d):
    return min(min(min(a, b), c), d)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
