import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        continue
    
    total_time = 0
    damage = 0  # accumulated damage
    
    for i in range(1, n):
        # damage gun i already received
        damage += p[i-1]
        
        if damage >= h[i]:
            continue
        else:
            # need extra time
            remaining = h[i] - damage
            extra = (remaining + p[i-1] - 1) // p[i-1]
            
            total_time += extra
            damage += extra * p[i-1]
    
    print(total_time)