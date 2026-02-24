
n = int(input())
splits = 0
for _ in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    blocks = data[1:]

    for i in range(k - 1):
        if blocks[i] > blocks[i + 1]:
            splits += 1

combines = (n + splits) - 1

print(splits, combines)

