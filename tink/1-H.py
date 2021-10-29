# Требуется определить, является ли данный год високосным. (Напомним, что год является високосным, если его номер
# кратен 4, но не кратен 100, а также если он кратен 400.)
#
# Входные данные
# Вводится единственное число - номер года (целое, положительное, не превышает 30000).
#
# Выходные данные
# Требуется вывести слово YES, если год является високосным и NO - в противном случае.
x = int(input())
if x % 100 == 0 and x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
    print("YES")
else:
    print("NO")