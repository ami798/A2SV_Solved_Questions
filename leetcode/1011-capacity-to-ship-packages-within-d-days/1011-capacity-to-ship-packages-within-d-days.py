class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if self.check(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left 

    def check(self, weights: List[int], days: int, capacity: int) -> bool:
        need_days = 1
        current = 0
        for w in weights:
            if current + w > capacity:
                need_days += 1
                current = 0
            current += w
        return need_days <= days