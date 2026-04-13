t = int(input())

for _ in range(t):
    n,k = list(map(int,input().split()))
    s =input()
    #s= input()
    count = s[:k].count('W')
    ans=count
    
    for i in range(k,n):
        if s[i] == 'W':
            count += 1
        if s[i-k] == 'W':
            count -= 1
        ans = min(count,ans)
    print(ans)


    
        
            


        

    
   