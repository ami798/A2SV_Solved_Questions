class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            if self.check(piles, h, mid):
                right = mid
            else:
                left = mid + 1
                
        return left

    def check(self, piles: List[int], h: int, speed: int) -> bool:
        total = 0
        
        for p in piles:
            total += (p + speed - 1) // speed
            if total > h:
                return False
                
        return True