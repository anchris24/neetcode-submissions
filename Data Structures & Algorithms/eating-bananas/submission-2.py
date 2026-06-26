class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        hours = float('inf')
        mid = -1
        got = False

        while left < right:
            mid = (left + right) // 2
            curr = 0
            for i in piles:
                curr += math.ceil(i / mid)

            hours = curr
            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid
        
        return left
            