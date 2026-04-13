t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = float('inf')

    for i in range(n):
        cnt_a = cnt_b = cnt_c = 0

        for j in range(i, min(i + 7, n)):
            if s[j] == 'a':
                cnt_a += 1
            elif s[j] == 'b':
                cnt_b += 1
            else:
                cnt_c += 1

            length = j - i + 1

            if length >= 2 and cnt_a > cnt_b and cnt_a > cnt_c:
                ans = min(ans, length)

    print(ans if ans != float('inf') else -1)