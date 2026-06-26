class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * (len(cost)+1)
        cost.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(len(cost)-2):
            dp[i+1] = min(dp[i+1], dp[i] + cost[i+1])
            dp[i+2] = min(dp[i+2], dp[i] + cost[i+2])
        # print(dp)
        
        return min(dp[-1], dp[-2])

