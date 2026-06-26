class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combos = []
        candidates.sort()

        def combosum(arr, total, startid):
            if total == target:
                combos.append(arr)
                return 
            
            if total > target:
                return

            for i in range(startid, len(candidates)):
                if i > startid and candidates[i] == candidates[i-1]:
                    continue
                combosum(arr + [candidates[i]], total + candidates[i], i+1)
            
        
        combosum([], 0, 0)

        return combos