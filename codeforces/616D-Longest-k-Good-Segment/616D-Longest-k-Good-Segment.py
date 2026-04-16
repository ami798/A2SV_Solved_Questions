from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = Counter()
left = 0

best_l = 0
best_r = 0

for right in range(n):
    cnt[a[right]] += 1   
    while len(cnt) > k:
        cnt[a[left]] -= 1
        if cnt[a[left]] == 0:
            del cnt[a[left]]
        left += 1
    if right - left > best_r - best_l:
        best_l = left
        best_r = right

print(best_l + 1, best_r + 1)