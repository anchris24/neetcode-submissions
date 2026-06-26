class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [0] * len(parents)

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(a, b):
            apar, bpar = find(a), find(b)
            if apar == bpar:
                return False    # same component
            
            if rank[apar] > rank[bpar]:
                parents[bpar] = apar
            elif rank[apar] < rank[bpar]:
                parents[apar] = bpar
            else:
                parents[apar] = bpar
                rank[apar] += 1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]


