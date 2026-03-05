class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0]*(n+1)
        
        for start,end,direction in shifts:
            if direction == 1:
                val = 1
            else:
                val = -1
                
            diff[start] += val
            diff[end+1] -= val
        
        
        shift = 0
        res = []
        
        for i in range(n):
            shift += diff[i]
            
            
            num = ord(s[i]) - ord('a')
            
           
            new = (num + shift) % 26
            
            res.append(chr(new + ord('a')))
        
        return "".join(res)