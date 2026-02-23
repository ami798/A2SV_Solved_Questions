

n = int(input())
books = [tuple(map(int, input().split())) for _ in range(n)]
prev_height = float('inf')
for w, h in books:
    
    if h <= prev_height and w <= prev_height:
        curr_height = max(h, w) if max(h, w) <= prev_height else min(h, w)
    elif h <= prev_height:
        curr_height = h
    elif w <= prev_height:
        curr_height = w
    else:
        print("NO")
        break
    prev_height = curr_height
else:
    print("YES")
    
    
    
    
            


    
























    #they are books in arow 
