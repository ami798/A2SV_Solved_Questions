from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 != 0:
            return []
        middle_num = (num - 3) // 3 + 1
        return [middle_num - 1, middle_num, middle_num + 1]
