class Solution:
    def myPow(self, x: float, n: int) -> float:
        newn = abs(n)

        def recurse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            if n%2 == 0:
                return recurse(x, n//2) ** 2
            else:
                return x * recurse(x, (n-1)//2) ** 2
        
        ans = recurse(x, newn)
        if n < 0:
            return 1 / ans
        return ans

            