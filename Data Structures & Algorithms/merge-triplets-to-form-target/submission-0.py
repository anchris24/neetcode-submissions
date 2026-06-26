class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x, y, z = target
        found = [False] * 3

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            
            if a == x:
                found[0] = True
            if b == y:
                found[1] = True
            if c == z:
                found[2] = True
        return all(found)
