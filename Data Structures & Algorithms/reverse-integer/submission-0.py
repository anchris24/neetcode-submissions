class Solution:
    def reverse(self, x: int) -> int:
        maxint = 2147483647
        minint = -2147483648
        x2 = abs(x)

        res = 0
        while x2 > 0:
            digit = x2%10

            if res * 10 > maxint or res * 10 < minint:
                return 0
            if (res == maxint // 10 and digit > maxint % 10) or (res == minint // 10 and digit < minint % 10):
                return 0
            
            res *= 10
            res += digit

            x2 //= 10
        
        return res if x > 0 else -res