t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print("NO")
        continue
    print("YES")
    
    res = []
    code = ord('A')
    for i in range(n // 2):
        c = chr(code)
        res.append(c)
        res.append(c)
        code += 1
    
    print("".join(res))