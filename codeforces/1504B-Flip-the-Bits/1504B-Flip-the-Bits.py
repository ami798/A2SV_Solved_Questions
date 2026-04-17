import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()
        balance = [0] * n
        ones = zeros = 0

        for i in range(n):
            if a[i] == '1':
                ones += 1
            else:
                zeros += 1
            balance[i] = ones - zeros

        flipped = False
        possible = True
        for i in range(n - 1, -1, -1):
            current = a[i]
            if flipped:
                current = '1' if current == '0' else '0'
            if current != b[i]:
                if balance[i] != 0:
                    possible = False
                    break
                flipped = not flipped  

        print("YES" if possible else "NO")


solve()