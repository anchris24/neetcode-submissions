class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        def dist(point):
            x, y = point[0], point[1]
            return ((x)**2 + (y)**2) ** 0.5

        for i in range(len(points)):
            heapq.heappush(heap, (-dist(points[i]), points[i]))
            if i >= k:
                heapq.heappop(heap)

        ans = []    
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
        
        
            
            