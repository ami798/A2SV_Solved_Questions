import sys

def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        permutation = []
        
        
        for i in range(1, n + 1):
            
            low = i
            median = n + (2 * i - 1)
            high = n + (2 * i)
            
            permutation.extend([low, median, high])
        
        results.append(" ".join(map(str, permutation)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()