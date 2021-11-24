# Напишите программу, которая разделяет входной поток чисел на кластеры – группы близких по значению чисел.
# Числа принадлежат одному кластеру, если расстояние между любыми соседними числами не больше заданного числа L ,
# а расстояние от любого числа данного кластера до любого числа другого кластера больше L .
# Исходные данные записаны в файл input.txt , результаты нужно вывести в файл output.txt .
#
# Входные данные
# В первой строке файла input.txt записаны числа N и L . Во второй строке записаны N элементов входного массива,
# разделённые пробелами.
#
# Выходные данные
# В первой строке файла output.txt нужно вывести число найденных кластеров K .
# В следующих K строчках выводятся элементы,входящие в каждый кластер, в порядке возрастания (неубывания).

class Cluster:

    def __init__(self, number, length):
        self.upper = number + length
        self.lower = number - length
        self.numbers = [number]

    def input(self, number, length):
        if self.lower <= number <= self.upper:
            if number + length > self.upper:
                self.upper = number + length
            if number - length < self.lower:
                self.lower = number - length
            self.numbers.append(number)
            return True
        else:
            return False

    def output(self):
        return sorted(self.numbers)

    def __repr__(self):
        return str(sorted(self.numbers)) + ' ' + str(self.lower) + ' ' + str(self.upper) + ';'


class ClusterGroup:

    def __init__(self, cluster):
        self.counter = 1
        self.sum = [cluster]

    def add(self, cluster):
        self.counter += 1
        self.sum.append(cluster)

    def out(self):
        return self.sum

    def count(self):
        return self.counter


f = open('input.txt', 'r', encoding='utf-8')
text = f.readlines()
f.close()
L = int(text[0].split()[1])
num = sorted([int(i) for i in text[1].split()])
x = Cluster(num[0], L)
xgr = ClusterGroup(x)
for i in num[1:]:
    f = 0
    for j in xgr.out():
        if j.input(i, L):
            f = 1
    if f == 0:
        x = Cluster(i, L)
        xgr.add(x)
for i in xgr.out():
    print(i)
f = open('output.txt', 'w')
f.write(str(xgr.count()) + '\n')
for i in xgr.out():
    for j in i.output():
        f.write(str(j) + ' ')
    f.write('\n')
f.close()
