t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    prefix = 0
    best_red = 0
    for x in r:
        prefix += x
        best_red = max(best_red, prefix)
   
    prefix = 0
    best_blue = 0
    for x in b:
        prefix += x
        best_blue = max(best_blue, prefix)
    
    print(best_red + best_blue)