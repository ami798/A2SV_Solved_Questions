import bisect

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))
    prev = -10**18
    ok = True
    for x in a:
        best = float('inf')

        
        if x >= prev:
            best = x

        
        idx = bisect.bisect_left(b, prev + x)
        if idx < m:
            best = min(best, b[idx] - x)

        if best == float('inf'):
            ok = False
            break

        prev = best

    print("YES" if ok else "NO")