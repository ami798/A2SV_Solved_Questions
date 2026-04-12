from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix):
            
            matrix[:] = list(zip(*matrix))
            
            matrix[:] = [list(row[::-1]) for row in matrix]
        
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False