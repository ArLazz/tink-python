# Для быстрого вычисления наибольшего общего делителя двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,amodb).
#
# Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).
#
# Входные данные
# Вводится два целых числа.
#
# Выходные данные
# Выведите ответ на задачу.

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a = int(input())
b = int(input())
print(gcd(a, b))