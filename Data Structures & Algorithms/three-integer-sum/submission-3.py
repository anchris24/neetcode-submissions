class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        if nums[-1] < 0:
            return []

        combos = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                currsum = nums[i] + nums[l] + nums[r]
                if currsum == 0:
                    combos.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
                elif currsum < 0:
                    l += 1
                else:
                    r -= 1
        
        return combos