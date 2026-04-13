t = int(input())
max_polygons = 0
for _ in range(t):
    n = int(input())
    sticks = list(map(int, input().split()))
    counts = {}
    for stick in sticks:
        counts[stick] = counts.get(stick, 0) + 1
    for k, v in counts.items():
        for i in range(3, v + 1):
            if v % i == 0:
                max_polygons = max(max_polygons, v // i)
print(max_polygons)