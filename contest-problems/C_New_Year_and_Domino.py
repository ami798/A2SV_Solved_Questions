

h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]

hor = [[0]*w for _ in range(h)]
ver = [[0]*w for _ in range(h)]


for i in range(h):
    for j in range(w-1):
        if grid[i][j]=='.' and grid[i][j+1]=='.':
            hor[i][j] = 1


for i in range(h-1):
    for j in range(w):
        if grid[i][j]=='.' and grid[i+1][j]=='.':
            ver[i][j] = 1


for i in range(h):
    for j in range(1,w):
        hor[i][j] += hor[i][j-1]

for j in range(w):
    for i in range(1,h):
        ver[i][j] += ver[i-1][j]

q = int(input())

for _ in range(q):
    r1,c1,r2,c2 = map(int,input().split())
    r1-=1;c1-=1;r2-=1;c2-=1

    ans = 0

    
    for i in range(r1,r2+1):
        ans += hor[i][c2-1] - (hor[i][c1-1] if c1>0 else 0)

   
    for j in range(c1,c2+1):
        ans += ver[r2-1][j] - (ver[r1-1][j] if r1>0 else 0)

    print(ans)