class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if word == s[i-1 : i + len(word) - 1] and dp[i-1]:
                    dp[i + len(word) - 1] = dp[i-1]
        return dp[-1]