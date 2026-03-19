class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        res = []
        for k in candies:
            res.append(k + extraCandies >= maxi)
        return res

        
        