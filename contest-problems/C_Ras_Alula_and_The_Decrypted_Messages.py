t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s= input()
    w = input()
    sum_t = 0
    for ch in w:
        sum_t += ord(ch)
        sum_window = 0
    for i in range(m):
        sum_window += ord(s[i])

    get = (sum_window == sum_t)

    for i in range(m, n):
        sum_window += ord(s[i])
        sum_window -= ord(s[i - m])

        if sum_window == sum_t:
            get = True

    print("YES" if get else "NO")