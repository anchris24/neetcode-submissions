class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        maxsize = [0]

        def bfs(r, c):
            queue = deque()
            size = 1
            queue.append((r, c))
            visited[r][c] = True
            

            while queue:
                cr, cc = queue.popleft()
                
                for dr, dc in directions:
                    if 0 <= cr + dr < len(grid) and 0 <= cc + dc < len(grid[0]):
                        if visited[cr + dr][cc + dc] or grid[cr + dr][cc + dc] == 0:
                            continue
                        queue.append((cr + dr, cc + dc))
                        visited[cr + dr][cc + dc] = True
                        size += 1
                        
            
            maxsize[0] = max(maxsize[0], size)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] or grid[r][c] == 0:
                    continue
                else:
                    bfs(r, c)

        return maxsize[0]

        

