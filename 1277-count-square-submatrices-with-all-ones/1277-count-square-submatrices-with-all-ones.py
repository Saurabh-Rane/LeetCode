class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        grid = [[0] * (n + 1) for i in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    grid[i + 1][j + 1] = min(grid[i][j + 1], grid[i + 1][j], grid[i][j]) + matrix[i][j]
                    res += grid[i + 1][j + 1]
                
        return res
        