class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i in range(len(board)):
            row = i - 1
            for j in range(len(board[0])):
                col = j - 1
                if (board[i][j] == 'X') and (row < 0 or board[row][j] == '.') and (col < 0 or board[i]                         [col] == '.'):
                    ans += 1
                    
        return ans