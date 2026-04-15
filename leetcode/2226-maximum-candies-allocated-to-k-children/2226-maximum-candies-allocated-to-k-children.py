class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = 0
        for c in candies:
            total += c
        
        if total < k:
            return 0

        left = 1
        right = max(candies)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            count = 0
            for c in candies:
                count += c // mid

            if count >= k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res