matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r, c = i, j

# Convert to 1-based index
r += 1
c += 1

print(abs(r - 3) + abs(c - 3))