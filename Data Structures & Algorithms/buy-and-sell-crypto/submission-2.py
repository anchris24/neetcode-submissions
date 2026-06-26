class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [float('inf')] * len(prices)
        dp[0] = prices[0]
        for i in range(1, len(prices)):
            dp[i] = min(dp[i-1], prices[i])
        
        maxm = 0
        for i in range(len(prices)):
            maxm = max(maxm, prices[i] - dp[i])
        return maxm