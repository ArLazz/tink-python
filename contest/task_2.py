n, m = [int(s) for s in input().split()]
x = 1
while n != m:
    if n > m:
        n -= m
    else:
        m -= n
    x += 1
print(x)