class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        for i in nums:
            prefix += i
            min_prefix = min(prefix, min_prefix)
        return 1 - min_prefix