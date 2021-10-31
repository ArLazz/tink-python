# В небоскребе n этажей. Известно, что если уронить стеклянный шарик с этажа номер p, и шарик разобъется,
# то если уронить шарик с этажа номер p+1, то он тоже разобъется. Также известно, что при броске с последнего этажа шарик
# всегда разбивается.
#
# Вы хотите определить минимальный номер этажа, при падении с которого шарик разбивается.
# Для проведения экспериментов у вас есть два шарика. Вы можете разбить их все, но в результате вы должны абсолютно точно
# определить этот номер.
#
# Определите, какого числа бросков достаточно, чтобы заведомо решить эту задачу.
#
# Входные данные
# Программа получает на вход количество этажей в небоскребе n
#
# Выходные данные
# Требуется вывести наименьшее число бросков, при котором можно всегда решить задачу.
#
# Тесты к этой задаче закрытые.
#
# Примечание
# Комментарий к первому примеру. Нужно бросить шарик со 2-го этажа. Если он разобъется, то бросим второй шарик с
# 1-го этажа, а если не разобъется - то бросим шарик с 3-го этажа.
#
# Подсказки.
# 1. Как следует действовать, если шарик был бы только один?
# 2. Пусть шариков два и мы бросили один шарик с этажа номер k. Как мы будем действовать в зависимости от того,
# разобъется ли шарик или нет?
# 3. Пусть f(n) - это минимальное число бросков, за которое можно определить искомый этаж, если бы в небоскребе
# было n этажей. Выразите f(n) через значения f(a) для меньших значений a.
from math import ceil as ceil, sqrt as sqrt
def func(level):
    if level < 2:
        return 0
    return ceil(0.5*sqrt(1 + 8 * (level - 1)) - 0.5)


level = int(input())
print(func(level))