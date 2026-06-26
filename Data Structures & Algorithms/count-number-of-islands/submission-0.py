class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        count = 0

        def explore(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0' or visited[r][c]:
                return
            visited[r][c] = True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                explore(r + dr, c + dc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and not visited[r][c]:
                    explore(r, c)
                    count += 1
        
        return count
                




