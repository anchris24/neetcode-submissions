class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjlist = [[] for _ in range(n)]
        for a, b, price in flights:
            adjlist[a].append((b, price))
        
        minprice = float('inf')

        queue = deque()
        queue.append((src, 0, -1))
        visited = [[float('inf'), float('inf')] for _ in range(n)]
        
        while queue:
            curr, price, stops = queue.popleft()
            if stops > k:
                continue
            if curr == dst:
                minprice = min(minprice, price)
            
            for neighbor, p in adjlist[curr]:    
                if price + p >= visited[neighbor][0] and stops + 1 >= visited[neighbor][1]:
                    continue
                visited[neighbor] = [price + p, stops + 1]
                queue.append((neighbor, price + p, stops + 1))
            
        return minprice if minprice != float('inf') else -1

            

