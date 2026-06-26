class Solution:
    def countSubstrings(self, s: str) -> int:
        
        cnt = 0

        for i in range(len(s) * 2 + 1):
            left, right = i // 2, i // 2 + i % 2

            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
        return cnt

        
        return cnt


