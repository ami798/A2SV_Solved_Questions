n = int(input())
weights = list(map(int, input().split()))
weights.sort()
total = sum(weights)
min_diff = total - 2 * weights[-1]
for i in range(n - 1):
    min_diff = min(min_diff, total - 2 * (weights[i] + weights[-1 - i]))
print(min_diff)