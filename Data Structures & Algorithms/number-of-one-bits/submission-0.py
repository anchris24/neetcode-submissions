class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            cnt += 1 if (1 << i) & n else 0
            print(cnt)
        return cnt