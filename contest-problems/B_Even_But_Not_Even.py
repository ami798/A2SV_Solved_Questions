t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    digits = [int(c) for c in s]
    
    i = n - 1
    while i >= 0 and digits[i] % 2 == 0:
        i -= 1
    if i < 0:
        print(-1)
        continue
    candidate = digits[:i+1]
   
    total = sum(candidate)
    if total % 2 == 0:
        print(''.join(str(d) for d in candidate))
    else:
        
        for j in range(len(candidate)-1):
            if candidate[j] % 2 == 1:
                result = candidate[:j] + candidate[j+1:]
                if result and result[-1] % 2 == 1 and sum(result) % 2 == 0:
                    print(''.join(str(d) for d in result))
                    break
        else:
            print(-1)

