t = int(input())
for _ in range(t):
    w = input().strip()
    p = int(input())
    price = sum(ord(c) - ord('a') + 1 for c in w)
    if price <= p:
        print(w)
        continue
    
    chars = [(ord(c) - ord('a') + 1, i) for i, c in enumerate(w)]
    
    chars.sort(key=lambda x: (-x[0], -x[1]))
    remove = set()
    for cost, i in chars:
        if price <= p:
            break
        price -= cost
        remove.add(i)
    
    res = [c for i, c in enumerate(w) if i not in remove]
    print(''.join(res))