class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target //= 2

        visited = set()
        visited.add(nums[0])

        for i in range(1, len(nums)):
            newvisit = set()
            for num in visited:
                newvisit.add(num)
                newvisit.add(num + nums[i])

            visited = newvisit
            
            if target in visited:
                return True
        
        return False

