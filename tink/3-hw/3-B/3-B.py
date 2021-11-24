# Напишите программу, которая моделирует работу стека целых чисел, управляемого текстовыми командами, аналогичными
# командам языка Форт. В начале работы стек пуст. Затем последовательно выполняются команды,
# записанные в файле input.txt.
# Для управления стеком используются команды:
# <число> – втолкнуть целое число на вершину стека
# DROP – удалить число с вершины стека
# SWAP – поменять местами два верхних числа в стеке (A B -> B A)
# DUP – дублировать верхнее число в стеке (A -> A A)
# OVER – скопировать второе число в стеке на вершину стека (A B -> A B A)
# '+' – сложить два верхних числа в стеке (A B -> A+B)
# '-' – вычесть из второго числа в стеке первое (A B -> A-B)
# '*' – перемножить два верхних числа в стеке (A B -> A*B)
# '/' – разделить второй число в стеке на первое (нацело) (A B -> A/B)
# Требуется определить состояние стека после окончания выполнения всех команд.
# Входные данные
# Входные строки в файле input.txt содержат команды управления стеком. Последняя строка файла пустая.
# Выходные данные
# Программа должна вывести в одной строке через пробел все числа, оказавшиеся в стеке после выполнения всех команд.
# Слева должно быть дно стека, справа – вершина. Если стек пуст, нужно вывести слово 'EMPTY'.
# Если во время выполнения команд произошла ошибка, нужно вывести слово 'ERROR'.
from functools import reduce


def error_function():
    s = open('output.txt', 'w')
    s.write('ERROR')
    s.close()
    exit()


class Stack:
    def __init__(self):
        self.st = []
        self.count = 0

    def add(self, number):
        self.st.append(number)
        self.count += 1

    def drop(self):
        if self.count >= 1:
            self.count -= 1
            self.st.pop(self.count)
        else:
            error_function()

    def swap(self):
        if self.count >= 2:
            self.st[-1], self.st[-2] = self.st[-2], self.st[-1]
        else:
            error_function()

    def dup(self):
        if self.count >= 1:
            self.st.append(self.st[-1])
            self.count += 1
        else:
            error_function()

    def over(self):
        if self.count >= 2:
            self.st.append(self.st[-2])
            self.count += 1
        else:
            error_function()

    def plus(self):
        if self.count >= 2:
            self.st[-2] += self.st[-1]
            self.count -= 1
            self.st.pop(self.count)
        else:
            error_function()

    def minus(self):
        if self.count >= 2:
            self.st[-2] -= self.st[-1]
            self.count -= 1
            self.st.pop(self.count)
        else:
            error_function()

    def multiply(self):
        if self.count >= 2:
            self.st[-2] *= self.st[-1]
            self.count -= 1
            self.st.pop(self.count)
        else:
            error_function()

    def div(self):
        if self.count >= 2:
            if self.st[-1] == 0:
                error_function()
            self.st[-2] //= self.st[-1]
            self.count -= 1
            self.st.pop(self.count)
        else:
            error_function()

    def __repr__(self):
        return str(reduce(lambda a, b: str(a) + ' ' + str(b), self.st))

    def empty(self):
        return self.count == 0


f = open('input.txt', 'r', encoding='utf-8')
text = f.read().splitlines()
f.close()
stack = Stack()
for i in text:
    if i.isdigit():
        stack.add(int(i))
    if i == 'DROP':
        stack.drop()
    if i == 'SWAP':
        stack.swap()
    if i == 'DUP':
        stack.dup()
    if i == 'OVER':
        stack.over()
    if i == '+':
        stack.plus()
    if i == '-':
        stack.minus()
    if i == '*':
        stack.multiply()
    if i == '/':
        stack.div()

f = open('output.txt', 'w')
if stack.empty():
    f.write('EMPTY')
else:
    f.write(str(stack))
f.close()
