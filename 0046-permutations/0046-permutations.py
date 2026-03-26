class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path, used, result):
            if len(path) == len(nums):
                result.append(path[:])  
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                
                used[i] = True
                path.append(nums[i])
                
                
                backtrack(path, used, result)
                
                
                path.pop()
                used[i] = False
        
        result = []
        used = [False] * len(nums)
        backtrack([], used, result)
        return result

       
