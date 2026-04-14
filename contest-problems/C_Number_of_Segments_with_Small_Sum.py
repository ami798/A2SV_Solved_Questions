n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
current_sum = 0
ans = 0

for r in range(n):
    current_sum += a[r]
    
    while current_sum > s:
        current_sum -= a[l]
        l += 1
    
    ans += (r - l + 1)

print(ans)