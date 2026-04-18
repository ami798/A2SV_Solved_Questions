import bisect

class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        nums = []
        cost = 0
        
        for x in instructions:
            left = bisect.bisect_left(nums, x)   
            right = len(nums) - bisect.bisect_right(nums, x)  
            
            cost += min(left, right)
            nums.insert(bisect.bisect_left(nums, x), x)
        
        return cost % MOD