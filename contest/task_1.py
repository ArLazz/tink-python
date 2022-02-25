a, b, n = [int(s) for s in input().split()]
if a <= b:
    print("NO")
elif (a + b) % 2 == 1:
    print("NO")
elif (a - b) // 2 < n:
    print("NO")
else:
    print("YES")