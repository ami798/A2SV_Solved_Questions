class Solution:
    def maxSumRangeQuery(self, nums, requests):
        MOD = 10**9 + 7
        n = len(nums)
        res = 0
        prefix = [0] * (n + 1)

        for l, r in requests:
            prefix[l] += 1
            if r + 1 < len(prefix):
                prefix[r+1] -= 1
        freq = [0] * n
        freq[0] = prefix[0]

        for i in range(1, n):
            freq[i] = freq[i-1] + prefix[i]
        nums.sort()
        freq.sort()
        for i in range(n):
            res = (res + nums[i] * freq[i]) % MOD

        return res