class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        maxlen = 1
        palin = s[0]

        for i in range(len(s) * 2 + 1):
            left, right = i // 2, i // 2 + i%2

            while 0 <= left and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
                    palin = s[left : right + 1]
                left -= 1
                right += 1

        return palin