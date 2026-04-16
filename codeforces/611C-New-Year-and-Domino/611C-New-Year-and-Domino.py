def get_sum(pref, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2:
        return 0
    return (pref[r2][c2]- pref[r1 - 1][c2]- pref[r2][c1 - 1]+ pref[r1 - 1][c1 - 1])
q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    ans = 0
    ans += get_sum(pref_hor, r1, c1, r2, c2 - 1)
    ans += get_sum(pref_ver, r1, c1, r2 - 1, c2)

    print(ans)