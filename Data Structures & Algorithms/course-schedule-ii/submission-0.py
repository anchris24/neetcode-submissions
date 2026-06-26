class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # toposort

        adjlist = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for x, y in prerequisites:
            indegrees[x] += 1
            adjlist[y].append(x)
        
        queue = [node for node in range(numCourses) if indegrees[node] == 0]
        schedule = []

        while queue:
            curr = queue.pop(0)
            schedule.append(curr)

            for neighbor in adjlist[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(schedule) == numCourses:
            return schedule
        return []


