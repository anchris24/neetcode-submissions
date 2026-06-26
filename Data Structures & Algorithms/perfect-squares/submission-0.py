class Solution:
    def numSquares(self, n: int) -> int:
        arr = [n] * (n+1)
        for num in range(int(n**0.5) + 1):
            arr[num*num] = 1
        
        for i in range(len(arr)):
            for sq in range(int(i**0.5) + 1):
                print(i, sq)
                arr[i] = min(arr[i], 1 + arr[i-sq*sq])

        return arr[-1]