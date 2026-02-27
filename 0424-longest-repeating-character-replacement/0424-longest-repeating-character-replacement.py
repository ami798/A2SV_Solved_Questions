class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        left = 0
        max_count = 0
        freq = defaultdict(int)
        result = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_count = max(max_count, freq[s[right]])

            
            while (right - left + 1) - max_count > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
