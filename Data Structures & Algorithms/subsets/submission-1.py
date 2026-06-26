class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sets = [[]]

        for curr in nums:
            sets += [s + [curr] for s in sets]
        
        return sets
