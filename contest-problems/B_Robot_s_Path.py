n,k=map(int,input().split())
road=input().strip()
count=0
for i in road:
    if i=='#':
        count+=1
        if count>=k:
            print("NO")
            break
    else:
        count=0
else:
    print("YES")

