class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        reachpac, reachatl = set(), set()
        queuepac, queueatl = deque(), deque()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r in range(len(heights)):
            queuepac.append( (r, 0) )
            queueatl.append( (r, len(heights[0]) - 1) )
        for c in range(len(heights[0])):
            queuepac.append( (0, c) )
            queueatl.append( (len(heights) - 1, c) )

        def bfs(queue, reach):
            
            while queue:
                cr, cc = queue.popleft()
                reach.add( (cr, cc) )
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if not (0 <= nr < len(heights) and 0 <= nc < len(heights[0])):
                        continue
                    if (nr, nc) in reach:
                        continue

                    if heights[nr][nc] >= heights[cr][cc]:
                        queue.append( (nr, nc) )
        
        bfs(queuepac, reachpac)
        bfs(queueatl, reachatl)

        ans = []
        for r in range(len(heights)):
             for c in range(len(heights[0])):
                if (r, c) in reachpac and (r, c) in reachatl:
                    ans.append([r, c])
        return ans

