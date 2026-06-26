class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        cnt = 0

        for i in range(len(s)):
            dp[i][i] = True
            cnt += 1
            if i != len(s) - 1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                cnt += 1
        
        print(cnt)
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                dp[i][i + length - 1] = dp[i+1][i + length - 2] and s[i] == s[i + length - 1]
                if dp[i][i + length - 1]:
                    cnt += 1
        
        print(dp)
        return cnt


