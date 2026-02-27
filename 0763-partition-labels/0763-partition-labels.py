class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result