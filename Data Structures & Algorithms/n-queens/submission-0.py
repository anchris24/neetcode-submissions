class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        posdiag, negdiag, col = set(), set(), set()
        
        def backtrack(rowid):
            if rowid == n:
                copy = [""] * n
                for i in range(n):
                    for j in range(n):
                        copy[i] += board[i][j]
                res.append(copy)
                return
            
            for c in range(len(board[0])):
                if c in col or rowid + c in posdiag or rowid - c in negdiag:
                    continue
                
                col.add(c)
                posdiag.add(rowid + c)
                negdiag.add(rowid - c)
                board[rowid][c] = 'Q'

                backtrack(rowid + 1)

                col.remove(c)
                posdiag.remove(rowid + c)
                negdiag.remove(rowid - c)
                board[rowid][c] = '.'
        
        backtrack(0)
        return res


