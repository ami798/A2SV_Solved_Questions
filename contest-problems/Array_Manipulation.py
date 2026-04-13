def arraymanipulation(n,queries):
    arr=[0]*(n*2)
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
    max_value=0
    current_sum=0
    for i in range(1,n+1):
        current_sum+=arr[i]
        max_value=max(max,current_sum)
    return max_value
    