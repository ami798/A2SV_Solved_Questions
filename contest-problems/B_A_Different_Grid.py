
t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	a = [list(map(int, input().split())) for _ in range(n)]
	total = n * m
	if total == 1:
		print(-1)
		continue
	
	f = []
	for row in a:
		f.extend(row)
	
	shifted = f[1:] + f[:1]
	
	idx = 0
	for i in range(n):
		print(' '.join(str(shifted[idx + j]) for j in range(m)))
		idx += m
