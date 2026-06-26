class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        sq = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                curr = int(board[r][c])-1
                if (1 << curr) & rows[r]:
                    return False
                if (1 << curr) & cols[c]:
                    return False
                if (1 << curr) & sq[r // 3 * 3 + c // 3]:
                    return False

                rows[r] |= 1 << curr
                cols[c] |= 1 << curr
                sq[r // 3 * 3 + c // 3] |= 1 << curr
        
        return True
