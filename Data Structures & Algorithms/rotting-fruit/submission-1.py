class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()
        maxdist = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append( (r, c, 0) )
        
        while queue:
            cr, cc, dist = queue.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                    continue
                
                if grid[nr][nc] != 1:
                    continue
                
                grid[nr][nc] = 2
                maxdist = max(maxdist, dist + 1)
                queue.append( (nr, nc, dist + 1))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return maxdist
