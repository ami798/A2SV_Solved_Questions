t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    def play(indices):
        if len(indices) == 1:
            return indices
        mid = len(indices) // 2
        left = play(indices[:mid])
        right = play(indices[mid:])
        left_sorted = sorted(left, key=lambda i: a[i])
        right_sorted = sorted(right, key=lambda i: a[i])
        wins = {}
        for i in left + right:
            wins[i] = 0
            # l vs r
        j = 0
        for i in left_sorted:
            while j < len(right_sorted) and a[right_sorted[j]] < a[i]:
                j += 1
            wins[i] += j
            # r vs l
        j = 0
        for i in right_sorted:
            while j < len(left_sorted) and a[left_sorted[j]] < a[i]:
                j += 1
            wins[i] += j
        for i in left + right:
            a[i] += wins[i]
        merged = left + right
        merged.sort(key=lambda i: a[i])
        return merged
    
    play(list(range(len(a))))
    print(*a)