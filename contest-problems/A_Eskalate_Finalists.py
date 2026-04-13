n = int(input())
ranks = list(map(int,input().split()))
ranks.sort()



dec = 0

for i in range(n):
    dec = max(dec,ranks[i] - (i+1))
print(dec)
