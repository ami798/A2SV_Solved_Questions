t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    if all(x == s[0] for x in s):
        ans = list(range(2, n+1)) + [1]
        print(' '.join(map(str, ans)))
    else:
        # If largest shoe size is unique, impossible
        if s[-1] > s[-2]:
            print(-1)
        else:
            ans = list(range(2, n+1)) + [1]
            print(' '.join(map(str, ans)))
            