class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumsquare(n):
            ans = 0
            while n > 0:
                ans += (n%10) ** 2
                n //= 10
            return ans
        
        fast, slow = sumsquare(n), n
        while slow != fast:
            print(slow, fast)
            fast = sumsquare(fast)
            fast = sumsquare(fast)

            slow = sumsquare(slow)
            
        return True if fast == 1 else False
            