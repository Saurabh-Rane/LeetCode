class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visitset = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i, j) in visitset:
                return 0
            
            visitset.add((i, j))
            perimeter = dfs(i + 1, j)
            perimeter += dfs(i - 1, j)
            perimeter += dfs(i, j + 1)
            perimeter += dfs(i, j - 1)
            
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
            