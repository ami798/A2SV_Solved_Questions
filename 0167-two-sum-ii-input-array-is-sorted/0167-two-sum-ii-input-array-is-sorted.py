class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        left,right=0,len(numbers)-1
        current_sum=0
        while left<right:
            current_sum=numbers[left]+numbers[right]
            if current_sum==target:
                return [left+1,right+1]
            elif current_sum<target:
                left+=1
            else:
                right-=1
            
        
            