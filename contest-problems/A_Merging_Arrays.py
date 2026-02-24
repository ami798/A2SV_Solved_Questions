n, m =map(int, input().split())
x =list(map(int, input().split()))
y =list(map(int, input().split()))
merged=[]
first,second=0,0
while first<len(x) and second<len(y):
    if x[first]<y[second]:
        merged.append(x[first])
        first+=1
    else:
        merged.append(y[second])
        second+=1
        

   





