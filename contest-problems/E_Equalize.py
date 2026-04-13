
t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	from collections import Counter
	freq = Counter()
	for i in range(n):
		freq[a[i] - i] += 1
	print(max(freq.values()))


