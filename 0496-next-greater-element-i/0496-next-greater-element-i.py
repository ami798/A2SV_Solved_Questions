class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        count = {}
        ans = []
        for i in range(len(nums2)):
            val = nums2[i]
            while stack and stack[-1] < val:
                out = stack.pop()
                count[out] = val
            stack.append(val)
        for i in nums1:
            if i not in count:
                ans.append(-1)
            else:
                ans.append(count[i])
        return ans


        