import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    good = []
    for idx, val in enumerate(a):
        if val < idx + 1:
            good.append(idx + 1)  
    ans = 0
    for j in range(n):
        if a[j] < j + 1:
            
            
            pos = bisect.bisect_left(good, j + 1)
            
            cnt = bisect.bisect_right(good, a[j], 0, pos)
            ans += pos - cnt
    print(ans)