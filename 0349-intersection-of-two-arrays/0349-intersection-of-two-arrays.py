class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash=set(nums1)
        last=[]
        for n in nums2:
            if n in hash:
                last.append(n)
                hash.remove(n)
        return last
                
        

        