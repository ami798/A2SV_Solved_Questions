class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        left = 0
        #sum = 0
        cnt = 0
        
        for right in range (len(nums)):
            sum = nums[right]
            while min_q and min_q[-1] > sum:
                min_q.pop()
            min_q.append(sum)
            while max_q and max_q[-1] < sum:
                max_q.pop()
            max_q.append(sum)
            while max_q[0] - min_q[0] > limit:
                if min_q[0] == nums[left]:
                    min_q.popleft()
                if max_q[0] == nums[left]:
                    max_q.popleft()
                left += 1
            cnt = max(cnt , right - left + 1)
        return cnt

        