from collections import Counter

class Solution:
    def findOriginalArray(self, changed):
        n = len(changed)

        if n % 2 != 0:
            return []

        cnt = Counter(changed)
        changed.sort()

        original = []

        for x in changed:
            if cnt[x] == 0:
                continue

            if cnt[2 * x] == 0:
                return []

            original.append(x)
            cnt[x] -= 1
            cnt[2 * x] -= 1

        return original