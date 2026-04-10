class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            for d in str(i):
                ans.append(int(d))
        return ans
           