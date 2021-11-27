# Напишите программу, которая строит матрицу смежности графа на основе списков смежности для каждой вершины.
#
# Входные данные
# В первой строке вводится количество вершин графа N ( 1≤ N ≤1000 ).
# 'В следующих N строках записаны списки смежности для каждой вершины – номера вершин,
# в которые существуют исходящие рёбра из данной вершины.
#
# Выходные данные
# Программа должна вывести матрицу смежности для заданного графа.


class Graph:
    def __init__(self):
        self.adjm = []

    # def __init__(self):
    #     self.al = defaultdict(list)
    # def pr_l(self):
    #     for i in self.al:
    #         for j in self.al[i]:
    #             if j != 0:
    #                 print(j, end=" ")
    #             else:
    #                 print(j, end=" ")
    #         print()
    #
    # def crfm(self, matrix, n):
    #     for i in range(n):
    #         f = True
    #         for j in range(n):
    #             if matrix[i][j] == 1:
    #                 self.al[i].append(j + 1)
    #                 f = False
    #         if f:
    #             self.al[i].append(0)
    def crfl(self, adjl, dim):
        self.adjm = [[0 for j in range(dim)] for i in range(dim)]
        for i in range(dim):
            for j in adjl[i]:
                if j != 0:
                    self.adjm[i][j - 1] = 1

    def pr_m(self):
        for i in range(len(self.adjm)):
            for j in range(len(self.adjm)):
                print(self.adjm[i][j], end=' ')
            print()


g = Graph()
n = int(input())
if 1 > n > 1000:
    exit()
m = []
for i in range(n):
    m.append([int(j) for j in input().split()])
g.crfl(m, n)
g.pr_m()
