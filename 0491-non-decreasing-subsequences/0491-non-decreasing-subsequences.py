class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack (start,path):
            if start >= len(nums):
                if len(path) > 1:
                    res.add(tuple(path[:]))
                return
            if not path or path[-1] <= nums[start]:
                path.append(nums[start])
                backtrack(start+1,path)
                path.pop()
            backtrack(start+1,path)
        backtrack(0,[])
        return list(res)



        