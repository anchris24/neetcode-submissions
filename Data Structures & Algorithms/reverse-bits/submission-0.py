class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            curr = (n >> i) & 1
            if curr:
                ans |= curr << (31 - i)
        return ans