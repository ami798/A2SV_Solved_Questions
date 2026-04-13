#t = int(input())
from collections import defaultdict
from random import randint

ran = randint(1, 1000000000)
t= int(input())
for _ in range(t):
	n, k = map(int, input().split())
	b_costs = defaultdict(list)
	
	
	for _ in range(k):
		b, c = map(int, input().split())
		b_costs[b ^ ran].append(c)
	b_sums = [sum(costs) for costs in b_costs.values()]
	b_sums.sort(reverse=True)
	
	print(sum(b_sums[:n]))
	
    

