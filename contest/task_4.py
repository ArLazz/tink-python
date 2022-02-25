def chess(n, m):
    if n <= 0 or m <= 0:
        return 0
    if n == m and n % 3 == 1:
        return 2 ** (n // 3)
    else:
        return chess(n - 1, m - 2) + chess(n - 2, m - 1)


n, m = [int(s) for s in input().split()]
print(chess(n, m))
