class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        pos = {}
        
        for i, val in enumerate(list1):
            pos[val] = i
        
        res = []
        min_sum = float('inf')
        
        for j, val in enumerate(list2):
            if val in pos:
                s = j + pos[val]
                
                if s < min_sum:
                    res = [val]
                    min_sum = s
                
                elif s == min_sum:
                    res.append(val)
        
        return res