class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can(distance):
            count = 1
            last = position[0]
            for i in range(len(position)):
                if position[i] - last >= distance:
                    count += 1
                    last = position[i]
                if count >= m:
                    return True
            return False
        left = 1
        right = position[-1] - position[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


      
        
        