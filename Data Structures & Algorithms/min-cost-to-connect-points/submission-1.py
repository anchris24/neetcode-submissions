class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlist = [[float('inf')] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                adjlist[i][j] = (abs(points[i][0] - points[j][0]) + 
                                abs(points[i][1] - points[j][1]))
        
        heap = []
        heapq.heapify(heap)
        visited = set()

        ans = 0
        heapq.heappush(heap, [0, 0])

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            ans += dist

            for n in range(len(adjlist[node])):
                heapq.heappush(heap, [adjlist[node][n], n])

        return ans


