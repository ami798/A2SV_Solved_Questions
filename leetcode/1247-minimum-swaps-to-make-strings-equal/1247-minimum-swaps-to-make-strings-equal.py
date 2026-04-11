class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        mismatches = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatches.append((s1[i], s2[i]))

        if len(mismatches) % 2 != 0:
            return -1

        xy = mismatches.count(('x', 'y'))
        yx = mismatches.count(('y', 'x'))

        return xy // 2 + yx // 2 + 2 * (xy % 2)