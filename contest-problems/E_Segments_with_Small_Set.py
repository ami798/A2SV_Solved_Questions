from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(int)
l = 0
unique = 0
ans = 0

for r in range(n):
 
    if freq[arr[r]] == 0:
        unique += 1
    freq[arr[r]] += 1

    
    while unique > k:
        freq[arr[l]] -= 1
        if freq[arr[l]] == 0:
            unique -= 1
        l += 1

   
    ans += (r - l + 1)

print(ans)