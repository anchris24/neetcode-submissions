class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        combos = []
        nums.sort()

        def backtrack(start, currsum, currcombo):
            if currsum == target:
                combos.append(currcombo)
                return 
            if currsum > target:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, currsum + nums[i], currcombo + [nums[i]])
                
            
        backtrack(0, 0, [])
        return combos