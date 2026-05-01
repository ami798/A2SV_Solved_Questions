from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())

    r = list(map(int, input().split()))
    r = [x - 1 for x in r]

    indegree = [0] * n
    rev = [[] for _ in range(n)]

    for u in range(n):
        v = r[u]

        indegree[v] += 1
        rev[v].append(u)

    
    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    in_cycle = [True] * n

    while q:

        u = q.popleft()

        in_cycle[u] = False

        v = r[u]

        indegree[v] -= 1

        if indegree[v] == 0:
            q.append(v)

    
    dist = [-1] * n
#d
    q = deque()

    for i in range(n):

        if in_cycle[i]:
            dist[i] = 0
            q.append(i)

    while q:

        u = q.popleft()

        for v in rev[u]:

            if dist[v] == -1:

                dist[v] = dist[u] + 1
                q.append(v)

    print(max(dist) + 2)