# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.
#
# Входные данные
# Программа получает на вход количество пар синонимов N.
# Далее следует N строк, каждая строка содержит ровно два слова-синонима. После этого следует одно слово.
#
# Выходные данные
# Программа должна вывести синоним к данному слову.
#
# Примечание
# Эту задачу можно решить и без словарей (сохранив все входные данные в списке),
# но решение со словарем будет более простым.
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])