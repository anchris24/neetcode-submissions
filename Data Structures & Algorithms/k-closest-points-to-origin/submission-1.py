class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x):
            return x[0] ** 2 + x[1] ** 2

        heap = []
        heapq.heapify(heap)

        for i in points:
            heapq.heappush(heap, (-dist(i), i))

            if len(heap) > k:
                heapq.heappop(heap)
            print(heap)

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans