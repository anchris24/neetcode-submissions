class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = set()

        def backtrack(path, idx):
            sets.add(path)
            if idx >= len(nums):
                return 

            backtrack(path, idx + 1)
            path += (nums[idx],)
            backtrack(path, idx + 1)
        
        backtrack((), 0)
        return [list(s) for s in sets]