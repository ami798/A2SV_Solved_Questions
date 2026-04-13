t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    
    if len(set(s)) == 1:
        print("NO")  
    elif n % 2 == 1 and len(set(s[:n//2])) == 1 and s[:n//2][0] == s[-1]: 
        
        print("NO")
    else:
        print("YES")