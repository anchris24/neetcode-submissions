class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        heap = [(grid[0][0], 0, 0)]
        visited = {(0,0)}

        while heap:
            maxsofar, r, c = heapq.heappop(heap)
            if r == len(grid)-1 and c == len(grid)-1:
                return maxsofar

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                if (nr, nc) in visited or not (0 <= nr < len(grid) and 0 <= nc < len(grid)):
                    continue

                visited.add((nr, nc))
                heapq.heappush(heap, (max(maxsofar, grid[nr][nc]), nr, nc))
        



        

