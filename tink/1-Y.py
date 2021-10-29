# Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C,
# сдвинув все элементы имевшие индекс не менее k вправо.
#
# Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет
# добавить новый элемент, используя метод append().
#
#Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного
# списка.
#
# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке. В следующей строке вводятся два целых числа.
#
# Выходные данные
# Выведите ответ на задачу.
a = [int(s) for s in input().split()]
k, c = [int(s) for s in input().split()]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = c
print(' '.join([str(i) for i in a]))