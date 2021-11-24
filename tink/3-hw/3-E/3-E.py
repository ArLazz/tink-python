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

class Graph:
    def __init__(self):
        self.vertex = []
        self.edges = []

    def out_vertices(self):
        return self.vertex

    def out_edges(self):
        return self.edges

    def add_vertex(self, vert):
        self.vertex.append(vert)

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_from_matrix(self, matrix, n):
        for i in range(n):
            self.vertex.append(i)
            for j in range(n):
                if matrix[i][j] == 1:
                    self.edges.append([i, j])

    def out_list(self):
        for i in self.vertex:
            f = 0
            for j in self.edges:
                if i == j[0]:
                    print(j[1] + 1, end=' ')
                    f = 1
            if f == 0:
                print(0)
            else:
                print()


g = Graph()
n = int(input())
if 1 > n > 1000:
    exit()
m = []
for i in range(n):
    m.append([int(j) for j in input().split()])
g.add_from_matrix(m, n)
g.out_list()
