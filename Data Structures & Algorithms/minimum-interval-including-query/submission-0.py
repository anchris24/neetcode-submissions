class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        queries = [(queries[i], i) for i in range(len(queries))]
        intervals.sort()
        queries.sort()

        ans = [-1] * len(queries)
        intervalsidx = 0
        queriesidx = 0
        heap = []
        heapq.heapify(heap)
        while queriesidx < len(queries):
            while intervalsidx < len(intervals) and queriesidx < len(queries) and intervals[intervalsidx][0] <= queries[queriesidx][0]:
                l, r = intervals[intervalsidx]
                heapq.heappush(heap, (r - l + 1, l, r))
                intervalsidx += 1
            
            while heap and heap[0][2] < queries[queriesidx][0]:
                heapq.heappop(heap)

            if heap:
                ans[queries[queriesidx][1]] = heap[0][0]
            queriesidx += 1
        
        return ans
