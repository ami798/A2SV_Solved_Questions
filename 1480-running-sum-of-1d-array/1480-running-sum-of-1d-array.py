class Solution:
    def runningSum(self, nums):
        res=[]
        total=0
        for n in nums:
            total+=n
            res.append(total)
        return res
