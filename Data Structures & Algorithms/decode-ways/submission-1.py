class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        first, second = 1, 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2, len(s) + 1):
            newval = 0
            if 1 <= int(s[i-1]) <= 9:
                newval += second
            if 10 <= int(s[i-2:i]) <= 26:
                newval += first
            first, second = second, newval
        return second

                


