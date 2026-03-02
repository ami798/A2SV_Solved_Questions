from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = Counter(a)
nums = sorted(cnt.keys())

max_cards = 0
left = 0
total = 0

for right in range(len(nums)):
    total += cnt[nums[right]]
    

    while nums[right] - nums[left] + 1 > k:
        total -= cnt[nums[left]]
        left += 1
        
    max_cards = max(max_cards, total)

print(max_cards)