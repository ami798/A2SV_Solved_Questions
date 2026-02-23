n,m=map(int,input().split())
total=0
com_total=0
savings=[]
for _ in range(n):
    a,b=map(int,input().split())
    total+=a
    com_total+=b
    savings.append(a-b)
if total<=m:
        print(0)
elif com_total>m:
        print(-1)
else:
        savings.sort(reverse=True)
        reduction_needed=total-m
        current_red=0
        count=0
        for s in savings:
            current_red+=s
            count+=1
            if current_red>=reduction_needed:
                print(count)
                break


