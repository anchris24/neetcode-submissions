class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(rate: int):
            time = 0
            for i in piles:
                add = (i/rate + (rate-1)/rate) // 1
                time += add
                print(add)
            return time
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2

            time = check(mid)
            print(lo, hi, mid, time)
            if time <= h:
                hi = mid
            else:
                lo = mid + 1
            
        return lo
