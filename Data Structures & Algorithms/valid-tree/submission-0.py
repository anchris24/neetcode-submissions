class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjlist = [[] for i in range(n)]
        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)

        visited = set()
        queue = []
        queue.append( (0, -1) )

        while queue:

            curr, parent = queue.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for i in adjlist[curr]:
                if i == parent:
                    continue
                if i in visited:
                    return False
                queue.append( (i, curr) )

        return len(visited) == n