n,s=map(int,input().split())
a=list(map(int,input().split()))
left=0
summation=0
count=0
for right in range(n):
    summation += a[right]
    while summation > s:
        summation -= a[left] 
        left += 1
    count += (right - left +1)
print(count)
