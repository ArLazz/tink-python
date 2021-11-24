# Напишите программу, которая моделирует колоду игральных карт. Сначала колода пуста. Затем выполняются команды,
# записанные в файле input.txt . Всего используется четыре команды:
# +<карта> – добавить карту на верх колоды
# ^ – снять верхнюю карту колоды
# #<карта> – добавить карту на дно колоды
# / – удалить нижнюю карту колоды
# Требуется определить, какие карты останутся в колоде после выполнения всех команд.
# Если во время работы произошла ошибка
# (удаляется карта из пустой колоды или добавляется карта, которая уже есть в колоде),
# нужно вывести слово 'ERROR'.
# Входные данные
# Входные строки файла input.txt содержат команды для управления колодой, по одной в каждой строка. Добавляемая карта
# обозначается кодом, состоящим из масти и ранга карты:
# <масть><ранг>
# Масть – это одна буква из следующего набора: 'C' (трефы, Clubs ), 'S' (пики, Spades ), 'H' (червы, Hearts ) и
# 'D' (бубны, Diamonds ).
# Ранг карты тоже обозначается одним знаком:
# A – туз ( Ace )
# 2-9 – карты ранга от 2 до 9 обозначаются цифрой
# T – десятка ( ten )
# J – валет ( Jack )
# Q – дама ( Queen )
# K – король ( King )
# Выходные данные
# Программа должна вывести коды всех карт, содержащихся в колоде, в одну строчку через пробел,
# начиная с верхней карты. Если произошла ошибка, нужно вывести слово 'ERROR'. Если колода пуста,
# нужно вывести слово 'EMPTY'.
from functools import reduce


def error_function():
    s = open('output.txt', 'w')
    s.write('ERROR')
    s.close()
    exit()


class DeckOfCards:
    def __init__(self):
        self.deck = []
        self.count = 0

    def add_up(self, card):
        if card in self.deck:
            error_function()
        self.deck.append(card)
        self.count += 1

    def add_down(self, card):
        if card in self.deck:
            error_function()
        self.deck.append(card)
        self.count += 1
        self.deck = self.deck[-1:] + self.deck[:-1]

    def drop_up(self):
        if self.count >= 1:
            self.count -= 1
            self.deck.pop(self.count)
        else:
            error_function()

    def drop_down(self):
        if self.count >= 1:
            self.count -= 1
            self.deck.pop(0)
        else:
            error_function()

    def __repr__(self):
        return str(reduce(lambda a, b: str(a) + ' ' + str(b), self.deck[::-1]))

    def empty(self):
        return self.count == 0


f = open('input.txt', 'r', encoding='utf-8')
text = f.read().splitlines()
f.close()
deck = DeckOfCards()
for i in text:
    if i[0] == '+':
        deck.add_up(i[1:])
    if i[0] == '^':
        deck.drop_up()
    if i[0] == '#':
        deck.add_down(i[1:])
    if i[0] == '/':
        deck.drop_down()
f = open('output.txt', 'w')
if deck.empty():
    f.write('EMPTY')
else:
    f.write(str(deck))
f.close()
