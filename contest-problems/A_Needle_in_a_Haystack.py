import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    t = input().strip()
    
    # Step 1: Count letters in t
    freq = [0] * 26
    for ch in t:
        freq[ord(ch) - ord('a')] += 1
    
    # Step 2: Remove letters of s
    possible = True
    for ch in s:
        idx = ord(ch) - ord('a')
        if freq[idx] == 0:
            possible = False
            break
        freq[idx] -= 1
    
    if not possible:
        print("Impossible")
        continue
    
    # Step 3: Build sorted remaining string
    remaining = ""
    for i in range(26):
        remaining += chr(i + ord('a')) * freq[i]
    
    # Step 4: Try two insertion strategies
    first = s[0]
    
    option1 = ""
    option2 = ""
    
    inserted1 = False
    inserted2 = False
    
    for ch in remaining:
        # Insert before first character >= s[0]
        if not inserted1 and ch >= first:
            option1 += s
            inserted1 = True
        option1 += ch
        
        # Insert before first character > s[0]
        if not inserted2 and ch > first:
            option2 += s
            inserted2 = True
        option2 += ch
    
    # If not inserted yet, append at end
    if not inserted1:
        option1 += s
    if not inserted2:
        option2 += s
    
    # Step 5: Print lexicographically smallest
    print(min(option1, option2))