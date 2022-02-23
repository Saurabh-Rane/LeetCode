class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRowVal = [0] * len(grid)
        maxColVal = [0] * len(grid)
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                maxRowVal[i] = max(maxRowVal[i], grid[i][j])
                maxColVal[j] = max(maxColVal[j], grid[i][j])
                
        for i in range(len(grid)):
            for j in range(len(grid)):
                res += min(maxRowVal[i], maxColVal[j]) - grid[i][j]
               
        return res
            
        