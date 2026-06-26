class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sets = []

        def subsetsum(arr, currsum, startid):
            if currsum == target:
                sets.append(arr)
                return
            
            for i in range(startid, len(nums)):
                if currsum + nums[i] > target:
                    continue
                
                subsetsum(arr + [nums[i]], currsum + nums[i], i)
        
        subsetsum([], 0, 0)
        return sets

            