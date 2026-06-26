class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]

        for x, y in prerequisites:
            adjlist[x].append(y)
        
        def dfs(start):
            queue = [start]
            visited = {start}

            while queue:
                curr = queue.pop(-1)
                for neighbor in adjlist[curr]:
                    if neighbor in visited:
                        return False
                    queue.append(neighbor)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

