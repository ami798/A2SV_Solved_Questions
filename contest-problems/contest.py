n, t = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
max_books = 0

for right in range(n):
    current_sum += arr[right]

    while current_sum > t:
        current_sum -= arr[left]
        left += 1

    max_books = max(max_books, right - left + 1)

print(max_books)




import sys
input = sys.stdin.readline

n, d = map(int, input().split())

friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append((m, s))

# Sort by money
friends.sort()

left = 0
current_sum = 0
max_sum = 0

for right in range(n):
    current_sum += friends[right][1]

    # If invalid (difference too large)
    while friends[right][0] - friends[left][0] >= d:
        current_sum -= friends[left][1]
        left += 1

    max_sum = max(max_sum, current_sum)

print(max_sum)



n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

alice_time = 0
bob_time = 0

alice_count = 0
bob_count = 0

while left <= right:
    if alice_time <= bob_time:
        alice_time += arr[left]
        alice_count += 1
        left += 1
    else:
        bob_time += arr[right]
        bob_count += 1
        right -= 1

print(alice_count, bob_count)






t=int(input())
n=list(map(int,input().split))
left=0
right=len(n)-1
while left<right:



    def can_form_another_palindrome(s):
    
    if len(set(s)) == 1:
        return False
    
    if s != s[::-1]:
        return True

    from collections import Counter
    cnt = Counter(s)
    odd = sum(1 for v in cnt.values() if v % 2)
    if (len(s) % 2 == 0 and odd == 0) or (len(s) % 2 == 1 and odd == 1):
        
        return True
    return False

t = int(input())
for _ in range(t):
    s = input().strip()
    print("YES" if can_form_another_palindrome(s) else "NO")
t=int(input())
n=int(input())
x=list(map(int,input().split()))
left=0
current_sum=0
for right in range(len(x)):
    current_sum+=min(x[right],x[right+1])
    while current_sum>0:
        current_sum-=x[left]+x[left+1]
        left-= 


        it is 