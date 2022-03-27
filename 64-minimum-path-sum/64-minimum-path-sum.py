class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        matrix = [[float('inf')] * (cols + 1) for i in range(rows + 1)]
        matrix[rows][cols -1] = 0
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                matrix[i][j] = grid[i][j] + min(matrix[i + 1][j], matrix[i][j + 1])
        
        return matrix[0][0]
                
        