class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = [[] for _ in range(n+1)]
        for a, b, time in times:
            edges[a].append( (b, time) )
        
        minheap = [(0, k)]
        heapq.heapify(minheap)
        visited = set()

        maxtime = 0
        
        while minheap:
            dist, curr = heapq.heappop(minheap)

            if curr in visited:
                continue
            print(dist, curr, visited)
            visited.add(curr)
            maxtime = dist
            for neighbor, time in edges[curr]:
                if neighbor not in visited:
                    heapq.heappush(minheap, (dist + time, neighbor))
        
        if len(visited) == n:
            return maxtime
        return -1
            


