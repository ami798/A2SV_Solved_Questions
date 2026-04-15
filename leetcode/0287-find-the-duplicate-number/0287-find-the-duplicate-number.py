from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for i in range(len(nums)):
            if cnt[i] > 1:
                return i
        