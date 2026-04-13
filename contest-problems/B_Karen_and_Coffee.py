n, k, q = map(int, input().split())
recipes = []
for _ in range(n):
    li, ri = map(int, input().split())
    recipes.append((li, ri))
admissible_counts = [0] * (200001)
for recipe in recipes:
    for i in range(recipe[0], recipe[1] + 1):
        admissible_counts[i] += 1
for _ in range(q):
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b + 1):
        if admissible_counts[i] >= k:
            count += 1
    print(count)