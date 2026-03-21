class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        fre = Counter(nums)
        for key, count in fre.items():
            if count * 2 > len(nums):
                dominant = key
                total_count = count
                break
        else:
            return -1

        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_count += 1
            if left_count * 2 > i + 1 and (total_count - left_count) * 2 > len(nums) - (i + 1):
                return i
        return -1

        