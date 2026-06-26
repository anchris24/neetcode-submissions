class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxdist = 0
        for i in range(len(nums)):
            if i <= maxdist:
                maxdist = max(maxdist, nums[i] + i)

        return maxdist >= len(nums) - 1