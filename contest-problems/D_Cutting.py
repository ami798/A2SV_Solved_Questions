n, B = map(int, input().split())
a = list(map(int, input().split()))

cuts = []
odd = even = 0

for i in range(n - 1):
    if a[i] % 2 == 0:
        even += 1
    else:
        odd += 1
    if odd == even:
        cuts.append(abs(a[i] - a[i + 1]))

cuts.sort()
ans = 0
for cost in cuts:
    if B >= cost:
        B -= cost
        ans += 1
    else:
        break

print(ans)