# Дан текст (строк может быть много). Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Входные данные
# Вводится текст.
#
# Выходные данные
# Выведите ответ на задачу.
c = {}
f = open('input.txt', 'r', encoding='utf-8')
text = f.readlines()
f.close()
l1 = str()
for i in range(len(text)):
    l1 = l1 + text[i]
l1 = l1.split()
for i in l1:
    c[i] = c.get(i, 0) + 1
m = max(c.values())
s = [k for k, v in c.items() if v == m]
print(min(s))
