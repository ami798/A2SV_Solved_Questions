t = int(input())
for _ in range(t):
    s = input().strip()
    from collections import Counter
    count = Counter(s)
    left = []
    
    for c in sorted(count):
        left.extend([c] * count[c])
    
    palindrome = ''.join(left + left[::-1])
    print(palindrome)