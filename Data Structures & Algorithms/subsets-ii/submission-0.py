class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        nums.sort()

        def backtrack(subset, start):
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subsets.append(subset + [nums[i]])
                backtrack(subset + [nums[i]], i+1)
        backtrack([], 0)
        return subsets