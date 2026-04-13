t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    correct = False
    stack = [n]
    while stack and stack[-1]:
        x = stack.pop()
        if x == m:
            correct = True
            break
        if x % 3 == 0 and x > m:
            stack.append(x//3)
            stack.append(x//3 * 2) 
    print("YES" if correct else "NO")
