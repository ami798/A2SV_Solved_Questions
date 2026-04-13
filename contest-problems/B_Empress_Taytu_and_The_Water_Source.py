def can(s, pairs, k):
    total = 0
    for a, d in pairs:
        trips = (d + s - 1) // s
        total += trips * a
        if total > k:
            return False
    return True


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    pairs = sorted(zip(a, d))

    l, r = 1, max(d)
    ans = -1
    if not can(r, pairs, k):
        print(-1)
        continue

    while l <= r:
        mid = (l + r) // 2
        if can(mid, pairs, k):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)