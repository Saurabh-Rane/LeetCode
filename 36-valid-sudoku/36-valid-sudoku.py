class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set) #key : (row // 3, col // 3)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col[j] or board[i][j] in row[i] or board[i][j] in square[(i // 3, j // 3)]:
                    return False
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                square[(i // 3, j // 3)].add(board[i][j])
                
        return True
        