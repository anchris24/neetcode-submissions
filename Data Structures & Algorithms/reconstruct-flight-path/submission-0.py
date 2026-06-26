class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adjlist = {}
        for i, j in tickets:
            if i not in adjlist:
                adjlist[i] = []
            adjlist[i].append(j)

        for lis in adjlist.values():
            heapq.heapify(lis)
        
        path = []
        # queue = ["JFK"]
        # while queue:
        #     curr = queue[-1]
        #     if not adjlist[curr]:
        #         path.append(curr)
        #         queue.remove(curr)
        #         continue
            
        #     while adjlist[curr]:
        #         queue.append(heapq.heappop(adjlist[curr]))

        def dfs(node):
            while node in adjlist and adjlist[node]:
                dfs(heapq.heappop(adjlist[node]))
            path.append(node)
        
        dfs("JFK")
        return path[::-1]