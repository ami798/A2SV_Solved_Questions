from collections import Counter
import math

class Solution:
    def numRabbits(self, answers):
        count = Counter(answers)
        rabbits = 0
        
        for x, c in count.items():
            group = x + 1
            rabbits += math.ceil(c / group) * group
        
        return rabbits
