class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0] * (n+2)
        mem[0] = 1

        for i in range(n):
            mem[i+1] += mem[i]
            mem[i+2] += mem[i]
            print(mem)
        
        return mem[n]