class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        ans = 0
        carry = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            bita = (a >> i) & 1
            bitb = (b >> i) & 1

            ans |= (bita ^ bitb ^ carry) << i
            carry = (bita + bitb + carry) >= 2
        
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ mask)
        
        return ans