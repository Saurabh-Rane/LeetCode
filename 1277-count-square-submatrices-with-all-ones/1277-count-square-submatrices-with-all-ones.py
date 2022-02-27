class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        row = len(matrix)
        col = len(matrix[0])
        submatrix = [[0] * (col + 1) for i in range(row + 1)] 
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    submatrix[i + 1][j + 1] = 1 + min(submatrix[i][j + 1], submatrix[i + 1][j], submatrix[i][j])
                    ans += submatrix[i + 1][j + 1]
                    
        return ans
        