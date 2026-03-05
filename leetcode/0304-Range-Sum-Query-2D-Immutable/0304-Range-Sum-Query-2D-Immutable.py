class NumMatrix:
#prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        self.prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for r in range(1, m+1):
            for c in range(1, n+1):
                self.prefix[r][c] = (
                    matrix[r-1][c-1]
                    + self.prefix[r-1][c]
                    + self.prefix[r][c-1]
                    - self.prefix[r-1][c-1]
                )

    def sumRegion(self, row1, col1, row2, col2):

        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        return (
            self.prefix[row2][col2]
            - self.prefix[row1-1][col2]
            - self.prefix[row2][col1-1]
            + self.prefix[row1-1][col1-1]
        )