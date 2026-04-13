n, k = map(int, input().split())

if k < 1 or k > 2 * n - 1:
    print(-1)
    exit()

a = [0] * n
cur = 1

def solve(l, r, need):
    global cur

    if l + 1 == r:
        a[l] = cur
        cur += 1
        return

    # if we only need 1 call → make sorted segment
    if need == 1:
        for i in range(l, r):
            a[i] = cur
            cur += 1
        return

    mid = (l + r) // 2

    left_size = mid - l
    right_size = r - mid

    # IMPORTANT FIX:
    # we DO NOT guess left/right arbitrarily
    # we greedily assign minimal possible to left

    for left_need in range(1, min(2 * left_size, need)):
        right_need = need - 1 - left_need

        if 1 <= right_need <= 2 * right_size - 1:
            solve(l, mid, left_need)
            solve(mid, r, right_need)
            return


solve(0, n, k)

print(*a)