class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:     


        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def backtrack(letterid, x, y):
            if used[x][y]:
                return False

            if word[letterid] != board[x][y]:
                return False
            else:
                if letterid == len(word) - 1:
                    return True

                used[x][y] = True
                if x < len(board) - 1 and backtrack(letterid + 1, x + 1, y):
                    return True
                if x > 0 and backtrack(letterid + 1, x - 1, y):
                    return True
                if y > 0 and backtrack(letterid + 1, x, y - 1):
                    return True
                if y < len(board[0]) - 1 and backtrack(letterid + 1, x, y + 1):
                    return True
                

                used[x][y] = False
                return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0, i, j):
                    return True

        return False