from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])
        
        def valid(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            
            left, left_count = valid(nums[:mid])
            right, right_count = valid(nums[mid:])
            
            total = left_count + right_count
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j] < left[i] - diff:
                    j += 1
                total += len(right) - j



            merged = []
            i = 0
            j = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged, total
        
        sorted_arr, answer = valid(arr)
        return answer