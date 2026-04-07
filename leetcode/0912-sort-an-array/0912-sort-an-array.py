from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        return self.mergeArray(left_half, right_half)
    
    def mergeArray(self, left_half, right_half):
        left, right = 0, 0
        merged = []
        
        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                merged.append(left_half[left])
                left += 1
            else:
                merged.append(right_half[right])
                right += 1
        
        while left < len(left_half):
            merged.append(left_half[left])
            left += 1
        
        while right < len(right_half):
            merged.append(right_half[right])
            right += 1
        
        return merged