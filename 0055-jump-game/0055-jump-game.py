class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        for i,jump in enumerate(nums):
            if i > maxi:
                return False
            
            maxi = max(maxi, i + jump)
        return True

        

                


        