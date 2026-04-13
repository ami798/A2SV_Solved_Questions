n = int(input())
s = input().strip()

if n == 1:
	print("Yes")
else:
	from collections import Counter
	cnt = Counter(s)
	if any(v >= 2 for v in cnt.values()):
		print("Yes")
	else:
		print("No")
