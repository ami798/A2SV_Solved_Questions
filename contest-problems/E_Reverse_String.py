q = int(input())
for _ in range(q):
    arr = input().strip()
    target = input().strip()
    n = len(arr)
    m = len(target)
    possible = False

    for i in range(n):
        for j in range(i, n):
            new = ""
            for k in range(i, j + 1):
                new += arr[k]
            for k in range(j - 1, -1, -1):
                new += arr[k]
            new = new[:m]
            if new == target:
                possible = True
                break
        
        if possible:
            break
    if possible:
        print("YES")
    else:
        print("NO")