class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        nums.sort()
        maxi = 0
        
        for i in range(n - 1):
            maxi = max(maxi, nums[i+1] - nums[i])
        
        return maxi