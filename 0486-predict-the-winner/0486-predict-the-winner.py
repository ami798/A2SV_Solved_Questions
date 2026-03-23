class Solution:
    def predictTheWinner(self, nums):
        
        def play(l, r, turn):
            if l > r:
                return 0
            
            if turn == 1:
                return max(
                    nums[l] + play(l+1, r, -1),
                    nums[r] + play(l, r-1, -1)
                )
            else:
                return min(
                    -nums[l] + play(l+1, r, 1),
                    -nums[r] + play(l, r-1, 1)
                )
        
        return play(0, len(nums)-1, 1) >= 0