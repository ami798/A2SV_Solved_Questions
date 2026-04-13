n,k = map(int,input().split())
s = input().strip()
weights = sorted(set(ord(c) - ord('a') + 1 for c in s))
res = 0
count = 0
last = -1
for i in weights:
    if i >= last + 2:
        res += i
        count += 1
        last = i
        if count == k:
            break
if count < k:
    print(-1)
else:

    print(res)