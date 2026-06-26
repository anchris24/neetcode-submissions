class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append( (r, c, 0) )
        
        while queue:
            cr, cc, dist = queue.popleft()
            for dr, dc in direc:
                nr, nc, = cr + dr, cc + dc
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                if grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] <= dist + 1:
                    continue
                
                grid[nr][nc] = dist + 1
                queue.append( (nr, nc, dist + 1) )
        


