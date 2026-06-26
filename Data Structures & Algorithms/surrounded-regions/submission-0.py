class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        queue = deque()

        for r in range(len(board)):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][-1] == 'O':
                queue.append((r, len(board[0])-1))
        for c in range(1, len(board[0]) - 1):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[-1][c] == 'O':
                queue.append((len(board)-1, c))

        while queue:
            cr, cc = queue.popleft()
            board[cr][cc] = '_'
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == 'O':
                        queue.append((nr, nc))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '_':
                    board[r][c] = 'O'
        

                    


