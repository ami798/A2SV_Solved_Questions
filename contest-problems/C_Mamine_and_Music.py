n, k = map(int, input().split())
a = list(map(int, input().split()))

pairs = sorted((a[i], i+1) for i in range(n))

ch = []
total = 0

for days, i in pairs:
    if total + days > k:
        break
    total += days
    ch.append(i)

print(len(ch))
print(*ch)