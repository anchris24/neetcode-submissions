class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        maxlen = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append( (r, c, 0) )
        
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = dr + r, dc + c
                
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):

                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    queue.append( (nr, nc, dist + 1) )
                    maxlen = max(maxlen, dist + 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return maxlen
