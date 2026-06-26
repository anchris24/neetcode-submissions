class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        lo, hi = 2500, 0
        for i in grid:
            hi = max(hi, max(i))
            lo = min(lo, min(i))
        
        def checkbfs(limit):
            if grid[0][0] > limit:
                return False
            queue = deque([(0,0)])
            visited = {(0,0)}

            while queue:
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid) - 1:
                    return True
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid) and (nr, nc) not in visited and grid[nr][nc] <= limit:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            print(lo, hi, mid)
            check = checkbfs(mid)

            if check:
                hi = mid
            else:
                lo = mid + 1
        
        return lo


        

