n,s=map(int,input().split())
a =list(map(int, input().split()))
left=0
count=0
sum=0
for right in range(len(s)):
    sum=left+right
    while sum<=s:
        count+=len(right,left)