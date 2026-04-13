import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    
    for _ in range(t):
        s = input().strip()
        n = len(s)
        q = int(input())
        queries = list(map(int, input().split()))
        
        res = []
        
        for k in queries:
            flip = 0
            
            while k > n:
                length = n
                while length * 2 < k:
                    length *= 2
                
                if k > length:
                    k -= length
                    flip ^= 1
                else:
                    
                    pass
            
            ch = s[k - 1]
            
            if flip:
                if ch.islower():
                    ch = ch.upper()
                else:
                    ch = ch.lower()
            
            res.append(ch)
        
        print(' '.join(res))

solve()