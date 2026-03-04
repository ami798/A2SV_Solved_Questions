class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum=0
        map={0:-1}
        
        for i in range(len(nums)):
            prefix_sum+= nums[i]
            seen = prefix_sum % k
            if seen in map:
                if i- map[seen] >=2:
                    return True
            else:
                map[seen]= i
        return False
                
                
                

            
        