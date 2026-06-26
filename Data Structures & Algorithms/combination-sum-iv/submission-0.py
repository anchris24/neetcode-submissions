class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                print(i, num)
                if i + num < len(dp):
                    dp[i + num] += dp[i]
        
        print(dp)
        return dp[-1]