from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        count = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(nums)):
            count[nums[right]] += 1

            if count[nums[right]] == 1:
                k -= 1

            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1

            res += right - left + 1

        return res