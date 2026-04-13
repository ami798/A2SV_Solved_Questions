t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mx = max(a)
    tot = [0] * (mx + 1)
    for x in a:
        tot[x] += 1
    ok = True
    for x in range(mx + 1):
        if tot[x] % k != 0:
            ok = False
            break
    if not ok:
        print(0)
        continue
    
    lim = [0] * (mx + 1)
    for x in range(mx + 1):
        if tot[x]:
            lim[x] = tot[x] // k
    cur = [0] * (mx + 1)
    l = 0
    ans = 0
    for r in range(n):
        v = a[r]
        cur[v] += 1
        
        while cur[v] > lim[v]:
            cur[a[l]] -= 1
            l += 1
        
        ans += (r - l + 1)
    
    print(ans)