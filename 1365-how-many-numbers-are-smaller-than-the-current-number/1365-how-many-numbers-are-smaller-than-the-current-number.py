from collections import Counter, defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        cnt = Counter(nums)

        array = sorted(cnt.keys())

        ans = [0]

        for i in range(1, len(array)):
            temp = array[i-1]
            ans.append(ans[-1] + cnt[temp])

        dct = defaultdict(int)

        for i in range(len(array)):
            dct[array[i]] = ans[i]

        res = []
        for i in range(len(nums)):
            res.append(dct[nums[i]])

        return res
