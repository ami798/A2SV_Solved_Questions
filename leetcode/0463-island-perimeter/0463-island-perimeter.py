class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        count -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        count -= 2

        return count