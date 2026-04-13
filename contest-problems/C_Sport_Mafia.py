n, k = map(int, input().split())
m = 0
while True:
    m += 1
    total = m * (m + 1) // 2
    e = n - m
    if total - e == k:
        print(e)
        break