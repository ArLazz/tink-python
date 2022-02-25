from math import ceil
n = int(input())
a = [int(s) for s in input().split()]
a.sort()
s = 0
for i in range(1,n + 1):
    s = (s + a[-i]) ** 0.5
print(ceil(s))