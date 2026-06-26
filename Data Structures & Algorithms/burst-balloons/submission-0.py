class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * (len(nums)) for _ in range(len(nums))]

        for length in range(1, len(nums) - 1):
            for i in range(len(nums) - length - 1):
                j = i + length + 1
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[k] * nums[i] * nums[j] + dp[i][k] + dp[k][j])
        
        return dp[0][-1]