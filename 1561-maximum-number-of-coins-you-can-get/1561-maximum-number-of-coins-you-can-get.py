class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        i = 0
        j = len(piles) - 2
        piles.sort()
        my_coins = 0
        while i < j:
            my_coins += piles[j]  
            i += 1
            j -= 2
        return my_coins  