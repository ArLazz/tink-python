# Напишите программу, которая строит списки смежности для каждой вершины графа на основе его матрицы смежности.
#
# Входные данные
# В первой строке вводится количество вершин графа N ( 1≤ N ≤1000 ). В следующих N строках записано по N чисел,
# разделённых пробелами – элементы матрицы смежности графа.
#
# Выходные данные
# Программа должна вывести списки смежности для каждой вершины графа в порядке возрастания их номеров.
# Номера вершин в каждом списке разделены пробелами. Нумерация начинается с единицы.
# Если из вершины не выходит ни одно ребро, вместо списка нужно вывести число 0.
from collections import defaultdict


class Graph:
    def __init__(self):
        self.al = defaultdict(list)
    def pr(self):
        for i in self.al:
            for j in self.al[i]:
                if j != 0:
                    print(j, end=" ")
                else:
                    print(j, end=" ")
            print()
    def crfm(self, matrix, n):
        for i in range(n):
            f = True
            for j in range(n):
                if matrix[i][j] == 1:
                    self.al[i].append(j + 1)
                    f = False
            if f:
                self.al[i].append(0)



g = Graph()
n = int(input())
if 1 > n > 1000:
    exit()
m = []
for i in range(n):
    m.append([int(j) for j in input().split()])
g.crfm(m, n)
g.pr()
