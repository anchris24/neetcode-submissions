class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append( (r, c, 0) )
        
        while q:
            r, c, dist = q.popleft()

            for dr, dc in [[-1, 0], [0, 1], [0, -1], [1, 0]]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = dist + 1
                    q.append( (nr, nc, dist + 1) )
        
