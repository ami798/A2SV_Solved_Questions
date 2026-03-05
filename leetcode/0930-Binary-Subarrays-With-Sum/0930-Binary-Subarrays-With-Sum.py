from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  

        for num in nums:
            prefix_sum += num
            count += prefix_map[prefix_sum - goal]
            prefix_map[prefix_sum] += 1

        return count