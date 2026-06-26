class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod, maxprod = nums[0], nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            min2, max2 = minprod, maxprod
            maxprod = max(nums[i], nums[i] * max2, nums[i] * min2)
            minprod = min(nums[i], nums[i] * max2, nums[i] * min2)

            ans = max(ans, maxprod)
            print(minprod, maxprod, ans)
        
        return ans
            
            

