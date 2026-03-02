t=int(input())


for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    score = 0
    
    for i in range(0, 2*n, 2):
        score += min(x[i], x[i+1])
    print(score)

