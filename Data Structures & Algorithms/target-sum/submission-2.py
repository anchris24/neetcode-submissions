class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited = {}
        visited[nums[0]] = visited.get(nums[0], 0) + 1
        visited[nums[0] * -1] = visited.get(nums[0]*-1, 0) + 1
        for i in range(1, len(nums)):
            nextvisit = {}
            curr = nums[i]

            for num, cnt in visited.items():
                nextvisit[num + curr] = nextvisit.get(num + curr, 0) + cnt
                nextvisit[num - curr] = nextvisit.get(num - curr, 0) + cnt
            
            visited = nextvisit
            print(visited)
            
        
        return visited.get(target, 0)