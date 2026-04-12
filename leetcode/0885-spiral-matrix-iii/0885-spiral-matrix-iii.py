from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        ans = []
        total = rows * cols
        
        # starting position
        r = rStart
        c = cStart
        
        ans.append([r, c])
        
        step = 1 
        direction = 0  
        
        while len(ans) < total:
            
            for _ in range(2):  
                
                for _ in range(step):
                    
                    
                    if direction == 0:   
                        c += 1
                    elif direction == 1: 
                        r += 1
                    elif direction == 2:
                        c -= 1
                    else:               
                        r -= 1
                    
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                    
                    if len(ans) == total:
                        return ans
                
                direction = (direction + 1) % 4
            
            step += 1  
        
        return ans