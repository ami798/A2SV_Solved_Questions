import heapq


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = []

    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))

    casinos.sort()  

    i = 0
    heap = []

    while True:
        # add all possible casinos
        while i < n and casinos[i][0] <= k:
            l, r, real = casinos[i]
            if k <= r:
                heapq.heappush(heap, -real)
            i += 1

        if not heap:
            break

        best = -heapq.heappop(heap)

        if best <= k:
            break

        k = best

    print(k)