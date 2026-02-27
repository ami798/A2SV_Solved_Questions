class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i = 0
        j = len(skill) - 1
        skill.sort()
        ans = 0
        sum = 0
        check = skill[0] + skill[-1]
        while i < j:
            sum = skill[i] + skill[j]
            if sum != check:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans
