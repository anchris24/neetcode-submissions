class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        clusters = [0]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def explore(r, c):
            queue = deque([(r, c)])

            while queue:
                currr, currc = queue.popleft()
                if visited[currr][currc]:
                    continue
                visited[currr][currc] = True

                for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    newr, newc = currr + dr, currc + dc
                    if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] == '1' and not visited[newr][newc]:
                        queue.append((newr, newc))
            clusters[0] += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c] and grid[r][c] == '1':
                    explore(r, c)
        return clusters[0]