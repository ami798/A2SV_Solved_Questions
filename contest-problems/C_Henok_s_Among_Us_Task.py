a,b = map(int,input().split())
seq = [b]
while b>a:
    if b % 2 == 0:
        b//=2
    elif b % 10 == 1:
        b//=10
    else:
        break
    seq.append(b)
if b==a:
    print("YES")
    print(len(seq))
    print(" ".join(map(str,reversed(seq))))
else:
    print("NO")