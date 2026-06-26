class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combos = []

        def backtrack(currsum, currcombo):
            if currsum == target:
                combos.append(currcombo)
                return
            
            if currsum > target:
                return
            
            for i in nums:
                if currcombo and i < currcombo[-1]:
                    continue
                backtrack(i + currsum, currcombo + [i])
            
        backtrack(0, [])
        return combos
            
            