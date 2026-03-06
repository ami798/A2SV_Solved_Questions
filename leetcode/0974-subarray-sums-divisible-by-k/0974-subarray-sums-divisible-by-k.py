class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        prefix_sum = 0
        count = [0] * k
        count[0] = 1
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            ans += count[remainder]
            
            
            count[remainder] += 1
            
        return ans