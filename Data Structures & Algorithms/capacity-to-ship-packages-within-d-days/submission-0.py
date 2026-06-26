class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low, high = max(weights), sum(weights)

        def daysreq(cap):
            count = 1
            curr = 0
            for w in weights:
                if cap < w:
                    return -1
                curr += w
                if curr > cap:
                    curr = w
                    count += 1
                
            return count
        
        while low < high:
            med = (low + high) // 2
            if daysreq(med) <= days:
                high = med
            elif daysreq(med) < 0 or daysreq(med) > days:
                low = med + 1
        
        return low