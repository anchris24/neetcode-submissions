class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            maxprev = 1
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i] and dp[j] + 1 > maxprev:
                    dp[i] = dp[j] + 1
                    maxprev = dp[i]
            
        return max(dp)
