from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        for i in range(len(s) - 1):
            first, second = s[i], s[i + 1]
            if first != second:
                if count[first] == int(first) and count[second] == int(second):
                    return first + second
        return ""
