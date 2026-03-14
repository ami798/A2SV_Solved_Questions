class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix[0])
        m=len(matrix)  
        transpose=[[0] * m for i in range(n) ]
        for i in range(m):
            for j in range (n):
                transpose[j][i]=matrix[i][j]
        return transpose     