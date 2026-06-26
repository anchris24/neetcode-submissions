class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        print(adj)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        # print(adj)
        count = 0
        visited = [False] * n
        queue = deque()
        for node in range(n):
            if visited[node]:
                continue
            
            queue.append(node)
            visited[node] = True
            while queue:
                curr = queue.popleft()
                for n in adj[curr]:
                    if visited[n]:
                        continue
                    queue.append(n)
                    visited[n] = True
            count += 1
        return count
        
                    
            