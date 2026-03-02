n,k=map(int,input().split())
a= list(map(int,input().split()))
left=0
unique=0
count=0
window=0
for right in range(n):
    unique+= a[right]
    window+=1
    while window>k:
        unique-=a[left]
        left+=1
    if unique == k:
        print(unique)
    

