class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]

        for x, y in prerequisites:
            adjlist[x].append(y)
        
        visited = [0] * numCourses
        def dfs(course):
            if visited[course] == -1:
                return False
            elif visited[course] == 1:
                return True

            visited[course] = -1
            for neighbor in adjlist[course]:
                if not dfs(neighbor):
                    return False
                
            visited[course] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

