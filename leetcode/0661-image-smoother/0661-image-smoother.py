class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n=len(img),len(img[0])
        result=[[0]*n for _ in range (m)]
        dir=[

            (0,0),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
        ]
        for i in range(m):
            for j in range(n):
                nei=[]
                for dx,dy in dir:
                    ni,nj=i+dx,j+dy
                    if 0<=ni<m and 0<=nj<n:
                        nei.append(img[ni][nj])
                        result[i][j]=sum(nei)//len(nei)
        return result

        